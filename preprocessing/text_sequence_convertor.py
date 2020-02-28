import pickle
import sys
from typing import Dict, List

import antlr4
import pandas as pd

from sql_parser.SqlBaseLexer import SqlBaseLexer
from preprocessing.build_vocabulary import get_common_words_dictionary
from preprocessing.tokens_map import reverseTokenMap, startToken, unknownToken, tokenMap
import torch

tokenTypesWithUniqueValues = {reverseTokenMap[s] for s in [
    "BINARY_LITERAL",
    "INTEGER_VALUE",
    "DECIMAL_VALUE",
    "IDENTIFIER",
    "DIGIT_IDENTIFIER",
    "QUOTED_IDENTIFIER",
    "BACKQUOTED_IDENTIFIER"]}


def text_to_seq(s: str, reverse_common_words_dictionary: Dict[str, int], i=None, omit_unknown=True):
    if i and i % 1000 == 0:
        print(f'iteration ${i}')
    unknownTokenCode = reverseTokenMap[unknownToken]
    startTokenCode = reverseTokenMap[startToken]

    input_stream = antlr4.InputStream(s)
    lex = SqlBaseLexer(input_stream)
    tokens = lex.getAllTokens()
    int_seq = [startTokenCode]
    for token in tokens:
        token_type = token.type
        text = token.text

        if (token_type == reverseTokenMap['WS']) or (token_type < 9):
            continue

        if token_type not in tokenTypesWithUniqueValues:
            int_seq.append(token_type)
            continue

        code = reverse_common_words_dictionary.get(text)
        if code is None:
            code = unknownTokenCode
            if omit_unknown:
                continue
        int_seq.append(code)
    return int_seq


def seq_to_text(seq: List[int], common_words_dictionary=None) -> str:
    if type(seq) == torch.Tensor:
        seq = seq.tolist()
    common_words_dictionary = common_words_dictionary or get_common_words_dictionary()[0]
    combined = {}
    combined.update(tokenMap)
    combined.update(common_words_dictionary)
    full_text = [(tokenMap.get(code) or common_words_dictionary.get(code)) for code in seq]
    return ' '.join(full_text)


def textCsv_to_SeqCsv(filename: str):
    common_words_dictionary, reverse_common_words_dictionary = get_common_words_dictionary()
    data = pd.read_csv(filename)['text']
    sequences = [text_to_seq(s, reverse_common_words_dictionary, i) for (i, s) in enumerate(data)]
    return sequences


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('usage: python text_sequence_convertor.py csvToSeq [csvFile] [outputFile]')
        exit(0)

    if sys.argv[1] == 'csvToSeq':
        csv_file = sys.argv[2]
        output_file_name = sys.argv[3]
        sequences = textCsv_to_SeqCsv(csv_file)

        with open(output_file_name, 'wb') as output_file:
            pickle.dump(sequences, output_file)
