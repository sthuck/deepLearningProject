import random
from typing import List, Dict

import torch

from preprocessing.build_final_dataset import DatasetItem
from .config import BATCH_SIZE


def get_batches_by_buckets(train: Dict[int, DatasetItem], batch_size=BATCH_SIZE):
    for seq_size in train.keys():
        dataset_items = train.get(seq_size)
        length = len(dataset_items)
        num_batches = length // batch_size
        for i in range(0, num_batches * batch_size, batch_size):
            dataset_items_batch = dataset_items[i: i + batch_size]
            dataset_sequences = [item.tensor for item in dataset_items_batch]
            dataset_lengths = torch.Tensor([item.length for item in dataset_items_batch])

            input_sequence = torch.stack(dataset_sequences)
            output_sequence = torch.zeros_like(input_sequence)
            output_sequence[:, :-1] = input_sequence[:, 1:]
            yield (input_sequence, dataset_lengths), output_sequence


def get_batches(train: Dict[int, List[DatasetItem]], shuffle=True, batch_size=BATCH_SIZE):
    batches = get_batches_by_buckets(train, batch_size)
    if shuffle:
        batches = list(batches)
        random.shuffle(batches)
    return batches
