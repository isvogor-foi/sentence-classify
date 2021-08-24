import random

from load_data import *

SENTENCES = ["I would like some PLACEHOLDER food",
             "Where can I find good PLACEHOLDER",
             "Find me a place that does PLACEHOLDER",
             "Which restaurants do PLACEHOLDER food",
             "Which restaurants do PLACEHOLDER food",
             "What is the weather like today"]
MAX_NGRAM = 2

if __name__ == '__main__':
    GEN_SIZE = 100000
    annnotated_sentence = []
    categories = read_categories()
    with open("../" + SENTECE_FILE_PATH, "w") as file, open("../" + LABELED_CSV_PATH, "w") as labeled_csv:
        for i in range(GEN_SIZE):
            random_sentence = random.randint(0, len(SENTENCES) - 1)
            random_category = random.randint(0, len(categories) - 1)
            category = categories[random_category]
            synthetic_sentence = SENTENCES[random_sentence].replace("PLACEHOLDER", category)
            if random_sentence == 5:
                random_category = len(categories) - 1
                category = categories[-1]
            print(synthetic_sentence)
            file.write(synthetic_sentence + "\n")
            labeled_csv.write(synthetic_sentence + "," + str(random_category) + "\n")
            annnotated_sentence.append({"input": synthetic_sentence, "category": category})

    with open("../" + ANNOTATED_DATASET_PATH, "w") as ml_file:
        out = json.dumps(annnotated_sentence)
        ml_file.write(out)
