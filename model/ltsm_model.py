from typing import Dict

import torch
import torch.nn as nn
from torch.nn.utils.rnn import pack_padded_sequence
from preprocessing.build_final_dataset import DatasetItem
from .config import BATCH_SIZE, COMPUTE_LOSS_EVERY_X_BATCHES, EMBEDDING_VECTOR_SIZE, LR, LSTM_LAYERS, STATE_SIZE, DROPOUT


class LSTMNet(nn.Module):
    def __init__(self, vocab_size, lstm_layers=LSTM_LAYERS, state_size=STATE_SIZE):
        super(LSTMNet, self).__init__()
        self.state_size = state_size
        self.lstm_layers = lstm_layers

        self.embedding = nn.Embedding(vocab_size, EMBEDDING_VECTOR_SIZE)
        self.lstm = nn.LSTM(EMBEDDING_VECTOR_SIZE,
                            self.state_size,
                            self.lstm_layers,
                            batch_first=True,
                            dropout=DROPOUT
                            )
        self.ff = nn.Linear(self.state_size, vocab_size)

    def forward(self, x, seq_length, pack_pad=False):
        x_embeddings = self.embedding(x)

        if pack_pad:
            x_embeddings = pack_padded_sequence(x_embeddings, seq_length, batch_first=True)

        output, state = self.lstm(x_embeddings)

        if pack_pad:
            output = output[0]

        output = self.ff(output)

        return output, state

    def zero_state(self, batch_size):
        return (torch.zeros(self.lstm_layers, batch_size, self.state_size),
                torch.zeros(self.lstm_layers, batch_size, self.state_size))

