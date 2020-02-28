from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

if __name__ == '__main__':
    model = Word2Vec.load('./data/word2vec.model')
    X = model[model.wv.vocab]
    pca = PCA(n_components=2)
    result = pca.fit_transform(X)
    pyplot.scatter(result[:, 0], result[:, 1])
    words = list(model.wv.vocab)
    interesting_words = ['uuid', 'msid', 'src', 'city', 'date', 'qbox', 'prod', 'sites', 'users']
    interesting_words_index = [(words.index(word), word) for word in interesting_words]

    for i, word in interesting_words_index:
        pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))

    pyplot.show()