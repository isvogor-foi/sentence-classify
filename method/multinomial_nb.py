from misc.load_data import read_annotated_dataset
from misc.stopwatch import stopwatch
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn.metrics import accuracy_score


@stopwatch("MultinomialNB")
def run(count_vect, clf, sentences, repeat=100):
    for k in range(repeat):
        for sentence in sentences:
            p = clf.predict(count_vect.transform([sentence]))
            # print(f"{sentence} ... {p}")


def train():
    df = read_annotated_dataset()
    df['category_id'] = df['category'].factorize()[0]

    train_input, test_input, train_output, test_output = train_test_split(df['input'],
                                                                          df['category'],
                                                                          random_state=0)
    # matrix of token counts
    count_vectorizer = CountVectorizer()

    train_input_counts = count_vectorizer.fit_transform(train_input)
    tfidf_transformer = TfidfTransformer()
    train_input_tfidf = tfidf_transformer.fit_transform(train_input_counts)

    # multinomial Naive Bayes
    clf = MultinomialNB().fit(train_input_tfidf, train_output)

    return count_vectorizer, clf

