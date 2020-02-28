import pandas as pd
import gensim, logging
from keras.preprocessing.text import text_to_word_sequence

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class SqlDataset:
    def __init__(self, filename):
        self.dataset = pd.read_csv(filename)

    def __iter__(self):
        for query in self.dataset['text']:
            yield text_to_word_sequence(query)


if __name__ == '__main__':
    sqlDataset = SqlDataset('./data/dataset-full.csv')
    model = gensim.models.Word2Vec(sqlDataset, window=20, min_count=5)
    model.save('./data/word2vec.model')


