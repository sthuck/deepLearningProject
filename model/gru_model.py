from typing import Dict

import torch
import torch.nn as nn
from torch.nn.utils.rnn import pack_padded_sequence
from preprocessing.build_final_dataset import DatasetItem
from .config import BATCH_SIZE, COMPUTE_LOSS_EVERY_X_BATCHES, EMBEDDING_VECTOR_SIZE, LR, LSTM_LAYERS, STATE_SIZE, DROPOUT


class GRUnet(nn.Module):
    def __init__(self, vocab_size, gru_layers=LSTM_LAYERS, state_size=STATE_SIZE):
        super(GRUnet, self).__init__()
        self.state_size = state_size
        self.gru_layers = gru_layers

        self.embedding = nn.Embedding(vocab_size, EMBEDDING_VECTOR_SIZE)
        self.gru = nn.GRU(EMBEDDING_VECTOR_SIZE,
                          self.state_size,
                          self.gru_layers,
                          batch_first=True,
                          dropout=DROPOUT
                          )
        self.ff = nn.Linear(self.state_size, vocab_size)

    def forward(self, x, input_lengths, pack_pad=False):
        x_embeddings = self.embedding(x)
        output, state = self.gru(x_embeddings)
        output = self.ff(output)
        return output, state

    def zero_state(self, batch_size):
        return (torch.zeros(self.gru_layers, batch_size, self.state_size),
                torch.zeros(self.gru_layers, batch_size, self.state_size))

