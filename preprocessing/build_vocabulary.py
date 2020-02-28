import pickle
import sys

from typing import List, Tuple, Sequence, Dict
from collections import Counter
import pandas as pd
from preprocessing.antlr_tokenizer import tokenize, tokenMap

BATCH = 30000
CORPUS_SIZE = 10000


###
# Poor man's parallelism. Read file by chunks, run this function multiple times
def build_word_counter(index: int):
    print(f'got index {index}')
    start = (index - 1) * BATCH
    end = index * BATCH
    print(f'got running on lines {start}-{end}')
    data = pd.read_csv('./data/dataset-valid-only.csv')['text']
    print(f'total lines: {len(data)}')

    token_stream, counter = tokenize(data[start: end])
    with open(f'./data/word-dictonary-{index}.pickle', 'wb') as outputfile:
        pickle.dump(counter, outputfile)


def join_vocabulary(how_many_files=4):
    counter = Counter()

    for index in range(1, how_many_files + 1):
        with open(f'./data/word-dictonary-{index}.pickle', 'rb') as input_file:
            mini_counter = pickle.load(input_file)
            counter = counter + mini_counter
    return counter


def build_common_words_dictionary(how_many_files):
    counter = join_vocabulary(how_many_files)
    common_words = counter.most_common(CORPUS_SIZE)
    index = 215  # Hard coded, the amount of keywords tokens we have
    word_mapping = {}
    for (word, count) in common_words:
        word_mapping[index] = word
        index += 1
    with open(f'./data/vocab.pickle', 'wb') as output_file:
        pickle.dump(word_mapping, output_file)


def get_common_words_dictionary():
    with open(f'./data/vocab.pickle', 'rb') as input_file:
        common_words_dictionary: Dict[int, str] = pickle.load(input_file)
        reverse_common_words_dictionary: Dict[str, int] = {v: k for k, v in common_words_dictionary.items()}
        return common_words_dictionary, reverse_common_words_dictionary


def main():
    if len(sys.argv) == 1:
        print('usage: python build_vocabulary.py build_word_counters [index]')
        print('usage: python build_vocabulary.py build_vocabulary [how many files]')
        exit(0)
    if sys.argv[1] == 'build_word_counters':
        index = int(sys.argv[2])
        build_word_counter(index)
    if sys.argv[1] == 'build_vocabulary':
        how_many_files = int(sys.argv[2])
        build_common_words_dictionary(how_many_files)


if __name__ == '__main__':
    main()
