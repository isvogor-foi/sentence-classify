from misc.load_data import read_sentences, read_categories
from method import naive, trie, multinomial_nb
from method import mlcnn

if __name__ == '__main__':
    sentences, categories = read_sentences(), read_categories()
    # check if reading went ok
    assert len(sentences) > 0 and len(categories) > 0, "There should be more sentences than categories"

    repeat = 1
    print("Running naive...")
    naive.run(sentences, categories, repeat)
    print("Running trie data structure...")
    trie.run(sentences, categories, repeat)
    count_vect, clf = multinomial_nb.train()
    print("Running multinomial_nb...")
    multinomial_nb.run(count_vect, clf, sentences, repeat)

    ml = mlcnn.MLCnn()
    # ml.train()
    print("Running cnn...")
    ml.load_trained_model()
    ml.inference(sentences, repeat)
