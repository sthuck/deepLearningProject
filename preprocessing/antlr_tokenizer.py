from collections import Counter, deque
from typing import Tuple, Sequence

import antlr4

from sql_parser.SqlBaseLexer import SqlBaseLexer
from preprocessing.tokens_map import reverseTokenMap, tokenMap, startToken, endToken

tokenTypesWithUniqueValues = {reverseTokenMap[s] for s in [
    "BINARY_LITERAL",
    "INTEGER_VALUE",
    "DECIMAL_VALUE",
    "IDENTIFIER",
    "DIGIT_IDENTIFIER",
    "QUOTED_IDENTIFIER",
    "BACKQUOTED_IDENTIFIER"]}


###
# Not really tokenize anymore, more like count unique words

def tokenize(seq: Sequence[str]):
    counter = Counter()
    token_sequences = []

    i = -1
    for s in seq:
        i += 1
        if (i % 2000) == 0:
            print(f'tokenize:: query {i}/{len(seq)}')

        input_stream = antlr4.InputStream(s)
        lex = SqlBaseLexer(input_stream)
        tokens = lex.getAllTokens()

        token_sequence: deque[Tuple[str, int]] = deque()
        token_sequence.append((startToken, reverseTokenMap[startToken]))

        for t in tokens:
            text: str = "''" if t.type is reverseTokenMap['STRING'] else t.text
            token_type: int = t.type
            if token_type in tokenTypesWithUniqueValues:
                counter[text] += 1

            token_sequence.append((text, token_type))

        token_sequence.append((endToken, reverseTokenMap[endToken]))
        token_sequences.append(token_sequence)
    return token_sequences, counter


def prettyPrint(s: str):
    input_stream = antlr4.InputStream(s)
    lex = SqlBaseLexer(input_stream)
    tokens = lex.getAllTokens()
    prettyTokens = [(t.text, tokenMap[t.type]) for t in tokens]
    return prettyTokens
