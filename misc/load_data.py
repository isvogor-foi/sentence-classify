import json

import pandas as pd

CATEGORY_FILE_PATH = "dataset_ext/categories.txt"
# STRUCTURED_CATEGORY_FILE_PATH = "dataset_ext/categories.json"
SENTECE_FILE_PATH = "dataset_ext/sentences.txt"
LABELED_CSV_PATH = "dataset_ext/data.csv"

def read_categories():
    categories = []
    with open(CATEGORY_FILE_PATH, "r") as file:
        [categories.append(x.strip().lower()) for x in file.readlines().__iter__()]
    return categories


# def read_structured_categories():
#     with open(STRUCTURED_CATEGORY_FILE_PATH, "r") as file:
#         return json.load(file)


def read_sentences():
    sentences = []
    with open(SENTECE_FILE_PATH, "r") as file:
        [sentences.append(x.strip().lower()) for x in file.readlines().__iter__()]
    return sentences


def get_ngram(sentence: str, n: int = 1):
    n_gram = []
    sentence = sentence.split(" ")
    for i in range(len(sentence) - (n - 1)):
        n_gram.append(" ".join(sentence[i:i + n]))
    return n_gram
