import pandas as pd
from misc.stopwatch import stopwatch
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


@stopwatch("MultinomialNB")
def run(count_vect, clf, sentences, repeat=100):
    for k in range(repeat):
        for sentence in sentences:
            p = clf.predict(count_vect.transform([sentence]))
            # print(f"{sentence} ... {p}")


def train():
    df = pd.read_csv("misc/data.csv")
    sentences = df['sentence'].values
    y = df['label'].values

    train_input, test_input, train_output, test_output = train_test_split(sentences, y,
                                                                          test_size=0.25,
                                                                          random_state=1000)

    # matrix of token counts
    count_vectorizer = CountVectorizer()

    train_input_counts = count_vectorizer.fit_transform(train_input)
    tfidf_transformer = TfidfTransformer()
    train_input_tfidf = tfidf_transformer.fit_transform(train_input_counts)

    # multinomial Naive Bayes
    clf = MultinomialNB().fit(train_input_tfidf, train_output)

    return count_vectorizer, clf
