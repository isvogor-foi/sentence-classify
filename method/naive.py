from misc.load_data import get_ngram
from misc.stopwatch import stopwatch

MAX_NGRAM = 2


@stopwatch("Naive")
def run(sentences, categories, repeat=100):
    # for each sentence, check occurance of n-grams
    for k in range(repeat):
        print(len(categories))
        for sentence in sentences:
            _categories = []
            for g in range(MAX_NGRAM):
                for gram in get_ngram(sentence, g + 1):
                    if gram in categories:
                        _categories.append(gram)
            # print(f"{sentence} is in {_categories}")
