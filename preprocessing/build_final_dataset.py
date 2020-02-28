from typing import List
import torch
import random
import math
from preprocessing.tokens_map import endToken, padToken, reverseTokenMap
import pickle
from collections import namedtuple

padTokenCode = reverseTokenMap[padToken]
endTokenCode = reverseTokenMap[endToken]

DatasetItem = namedtuple('DatasetItem', 'tensor length')


# split to buckets
# pad lengths
# put endToken at end
def pad_and_split_to_buckets(tensors: List[DatasetItem]):
    by_length: dict[int, List[DatasetItem]] = {}
    for tensor in tensors:
        length = len(tensor)
        round_length = math.ceil((length + 1) / 200) * 200  # +1 to save a place for end token
        new_tensor = torch.nn.functional.pad(tensor, (0, round_length - length), mode='constant', value=padTokenCode)
        new_tensor[length] = endTokenCode
        list_by_length = by_length.get(round_length) or []
        list_by_length.append(DatasetItem(new_tensor, length))
        by_length[round_length] = list_by_length
    return by_length


def default_dataset(filename='./data/dataset-seq.pickle'):
    with open(filename, 'rb') as input_file:
        return pickle.load(input_file)


# shuffle dataset
# split to batches according to similar length
# pad all sequences in a batch to have the same length

def final_dataset(seqs: List[List[int]] = None, max_length=3000, train_test_split=0.9, item_limit=None):
    seqs = seqs or default_dataset()
    if item_limit:
        seqs = seqs[:item_limit]
    # seqs = map(lambda seq: list(filter(lambda code: code >= 9, seq)), seqs)
    tensors = [torch.Tensor(s) for s in seqs if len(s) < max_length]
    random.shuffle(tensors)

    # split 90-10, training-test
    total = len(tensors)
    total_train = round(total * train_test_split)

    train = tensors[0:total_train]
    test = tensors[total_train:]
    return train, test
