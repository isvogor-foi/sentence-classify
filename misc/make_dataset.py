import itertools
import random

from load_data import *

CATEGORIES = []
SYNTHETIC_CATEGORIES = []

SENTENCES = ["I would like some PLACEHOLDER food",
             "Where can I find good PLACEHOLDER",
             "Find me a place that does PLACEHOLDER",
             "Which restaurants do PLACEHOLDER food",
             "Which restaurants do PLACEHOLDER food",
             "What is the weather like today"]
MAX_NGRAM = 2

if __name__ == '__main__':
    GEN_SIZE = 100000
    # _categories = read_structured_categories()
    # with open("../" + CATEGORY_FILE_PATH, "w") as file:
    #     world_parts = _categories["world"]
    #     food_types = _categories["type"]
    #     r = list(itertools.product(world_parts, food_types))
    #     print(r)
    #     for i in r:
    #         rand = random.randint(0, 10)
    #         if rand > 3:
    #             synthetic_category = i[0] + " " + i[1]
    #         elif rand > 7:
    #             synthetic_category = i[1]
    #         else:
    #             synthetic_category = i[0]
    #         if synthetic_category not in SYNTHETIC_CATEGORIES:
    #             file.write(synthetic_category + "\n")
    #             SYNTHETIC_CATEGORIES.append(synthetic_category)
    #     file.write("None" + "\n")
    #     SYNTHETIC_CATEGORIES.append("None")

    annnotated_sentence = []
    SYNTHETIC_CATEGORIES.clear()
    SYNTHETIC_CATEGORIES = read_categories()
    with open("../" + SENTECE_FILE_PATH, "w") as file, open("data.csv", "w") as file2:
        for i in range(GEN_SIZE):
            random_sentence = random.randint(0, len(SENTENCES) - 1)
            random_category = random.randint(0, len(SYNTHETIC_CATEGORIES) - 1)
            category = SYNTHETIC_CATEGORIES[random_category]
            synthetic_sentence = SENTENCES[random_sentence].replace("PLACEHOLDER", category)
            if random_sentence == 5:
                random_category = len(SYNTHETIC_CATEGORIES) - 1
                category = SYNTHETIC_CATEGORIES[-1]
            print(synthetic_sentence)
            file.write(synthetic_sentence + "\n")
            file2.write(synthetic_sentence + "," + str(random_category) +"\n")
            annnotated_sentence.append({"input": synthetic_sentence, "category": category})

    with open("../" + ANNOTATED_DATASET_PATH, "w") as ml_file:
        out = json.dumps(annnotated_sentence)
        ml_file.write(out)
