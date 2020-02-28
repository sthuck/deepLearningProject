from collections import deque

import pandas as pd
import torch
import torch.nn as nn

from preprocessing.antlr_tokenizer import tokenMap
from preprocessing.build_final_dataset import final_dataset, pad_and_split_to_buckets
from preprocessing.text_sequence_convertor import get_common_words_dictionary, text_to_seq, seq_to_text
from model.batches import get_batches
from model.config import BATCH_SIZE, COMPUTE_LOSS_EVERY_X_BATCHES, LR, TOTAL_EPOCHS, ITEM_LIMIT,MAX_SEQUENCE_LENGTH
from model.ltsm_model import LSTMNet
from model.gru_model import GRUnet
from torch.nn.utils.rnn import pack_padded_sequence
import time
PACK_PAD = False


# for tpu
# import torch_xla.core.xla_model as xm

def eval(net: LSTMNet, testset, device):
    net.eval()

    criterion = nn.CrossEntropyLoss()

    test_loss = 0
    counter = 0
    with torch.no_grad():
        for (input_seq, input_lengths), target_seq in get_batches(testset, batch_size=8):
            counter += 1

            input_seq = input_seq.long().to(device)
            input_lengths = input_lengths.long().to(device)
            target_seq = target_seq.long().to(device)

            result, (state_h, state_c) = net(input_seq, input_lengths, pack_pad=PACK_PAD)
            test_loss += criterion(result.transpose(1, 2), target_seq).item()

    avg_loss = test_loss / counter
    net.train()
    return avg_loss


def predict_word(device, reverse_common_words_dictionary, common_words_dictionary):
    def predictor(net: LSTMNet, query: str, top_k=5):
        net.eval()
        seq = text_to_seq(query, reverse_common_words_dictionary)

        state_h, state_c = net.zero_state(1)
        state_h = state_h.to(device)
        state_c = state_c.to(device)
        for code in seq:
            x = torch.tensor([[code]]).to(device)
            output, (state_h, state_c) = net(x, (state_h, state_c))

        _, top_ix = torch.topk(output[0], k=top_k)
        choices = top_ix.tolist()[0]
        options = [seq_to_text([code], common_words_dictionary) for code in choices]

        print(options)
        net.train()
    return predictor


def predict_full_text(device):
    def predictor(net: LSTMNet, seq, top_k=5):
        net.eval()

        state_h, state_c = net.zero_state(1)
        state_h = state_h.to(device)
        state_c = state_c.to(device)
        total = 0
        accurate = 0
        accurate_top = 0
        with torch.no_grad():
            for i, code in enumerate(seq):
                if code == 0 or i == (len(seq) -1):
                    break
                x = torch.tensor([[code]]).long().to(device)
                output, (state_h, state_c) = net(x, (state_h, state_c))

                _, top_ix = torch.topk(output[0], k=top_k)
                top_ix = top_ix.tolist()[0]
                _, top_1 = torch.topk(output[0], k=1)
                top_1 = top_1.tolist()[0]
                next_token = seq[i+1]

                total += 1
                if next_token in top_1:
                    accurate += 1
                if next_token in top_ix:
                    accurate_top += 1
        net.train()
        return accurate/total, accurate_top/total
    return predictor


def main():
    common_words_dictionary, reverse_common_words_dictionary = get_common_words_dictionary()
    total_vocabulary_size = len(common_words_dictionary) + len(tokenMap)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    # device = xm.xla_device()

    predictor = predict_word(device, reverse_common_words_dictionary, common_words_dictionary)
    full_text_predictor = predict_full_text(device)

    trainset, testset = final_dataset(max_length=MAX_SEQUENCE_LENGTH, item_limit=ITEM_LIMIT)
    train_buckets = pad_and_split_to_buckets(trainset)
    test_buckets = pad_and_split_to_buckets(testset)

    net = GRUnet(total_vocabulary_size)
    net = net.to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(net.parameters(), lr=LR, betas=(0.9, 0.999))

    iteration = 0
    running_loss = 0.0
    train_losses_x = deque()
    train_losses_y = deque()
    test_losses_x = deque()
    test_losses_y = deque()

    start_time = time.time()
    for e in range(TOTAL_EPOCHS):
        for (input_seq, input_lengths), target_seq in get_batches(train_buckets):

            iteration += 1
            net.train()

            optimizer.zero_grad()

            input_seq = input_seq.long().to(device)
            input_lengths = input_lengths.long().to(device)
            target_seq = target_seq.long().to(device)

            if PACK_PAD:
                input_lengths, idx_sort = torch.sort(input_lengths, dim=0, descending=True)
                input_seq = torch.index_select(input_seq, dim=0, index=idx_sort)
                target_seq = pack_padded_sequence(target_seq, input_lengths, batch_first=True)

            result, (state_h, state_c) = net(input_seq, input_lengths, pack_pad=PACK_PAD)

            if PACK_PAD:
                loss = criterion(result, target_seq[0])
            else:
                loss = criterion(result.transpose(1, 2), target_seq)

            loss.backward()

            # _ = torch.nn.utils.clip_grad_norm_(
            #     net.parameters(), 5)

            optimizer.step()
            # xm.optimizer_step(optimizer, barrier=True)

            running_loss += loss.item()
            if iteration % COMPUTE_LOSS_EVERY_X_BATCHES == 0:
                average_loss = running_loss / COMPUTE_LOSS_EVERY_X_BATCHES
                print('Epoch: {}/{}'.format(e, TOTAL_EPOCHS),
                      'Iteration: {}'.format(iteration),
                      'Avg. Loss: {}'.format(average_loss))
                train_losses_y.append(running_loss / COMPUTE_LOSS_EVERY_X_BATCHES)
                train_losses_x.append(iteration)
                predictor(net, 'select ')
                running_loss = 0.0

        avg_loss = eval(net, test_buckets, device)
        test_losses_y.append(avg_loss)
        test_losses_x.append(iteration)
        print(f'avg_loss on epoch {e}: {avg_loss}')

    total_time = time.time() - start_time
    print(f'total time: {total_time}')

    compute_accuracy(full_text_predictor, net, testset)
    torch.save(net.state_dict(), './data/lstm_model.torch')

    return test_losses_x, test_losses_y, train_losses_x, train_losses_y, total_time


def compute_accuracy(full_text_predictor, net, testset):
    accuracy_subset_test = testset[: 2000]
    accuracy = 0
    accuracy_top = 0
    for seq in accuracy_subset_test:
        accuracy_, accuracy_top_ = full_text_predictor(net, seq, top_k=5)
        accuracy += accuracy_
        accuracy_top += accuracy_top_
    accuracy = accuracy / 2000
    accuracy_top = accuracy_top / 2000
    print(accuracy)
    print(accuracy_top)


if __name__ == '__main__':
    test_losses_x, test_losses_y, train_losses_x, train_losses_y, total_time = main()
    te = pd.DataFrame({'test_loss': test_losses_y}, index=test_losses_x)
    tr = pd.DataFrame({'train_loss': train_losses_y}, index=train_losses_x)
    te.to_csv('./data/test_loss.csv')
    tr.to_csv('./data/train_loss.csv')
