# import numpy as np
# from tokenizers.tokens_map import padToken, reverseTokenMap, unknownToken
#
# padTokenCode = reverseTokenMap[padToken]
# unknownTokenCode = reverseTokenMap[unknownToken]
#
#
# def token_seq_to_windowed_seq(seq: np.ndarray, windowSize: int):
#     inputs = []
#     targets = []
#     for i in range(len(seq) - 1):
#         if seq[i] == unknownTokenCode:
#             continue
#         if i > windowSize:
#             inputs.append(seq[i - windowSize: i])
#         else:
#             partial = seq[0: i+1]
#             inputs.append(np.pad(partial, (0, windowSize-i), mode='constant', constant_values=padTokenCode))
#         targets.append(seq[i+1])
#     return inputs, targets
#
#
#
