import numpy as np
import pandas as pd
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from misc.stopwatch import stopwatch
from sklearn.model_selection import train_test_split
from tensorflow import keras


class MLCnn:
    def __init__(self):
        df = pd.read_csv("misc/data.csv")
        sentences = df['sentence'].values
        y = df['label'].values

        self.sentences_train, self.sentences_test, self.y_train, self.y_test = train_test_split(sentences, y,
                                                                                                test_size=0.25,
                                                                                                random_state=1000)

        self.tokenizer = Tokenizer(num_words=5000)
        self.tokenizer.fit_on_texts(self.sentences_train)

        self.X_train = self.tokenizer.texts_to_sequences(self.sentences_train)
        self.X_test = self.tokenizer.texts_to_sequences(self.sentences_test)

        # Adding 1 because of  reserved 0 index
        self.vocab_size = len(self.tokenizer.word_index) + 1

        self.maxlen = 100

        self.X_train = pad_sequences(self.X_train, padding='post', maxlen=self.maxlen)
        self.X_test = pad_sequences(self.X_test, padding='post', maxlen=self.maxlen)

        self.embedding_dim = 50
        self.embedding_matrix = self.create_embedding_matrix("method/.vector_cache/glove.6B.100d.txt",
                                                             self.tokenizer.word_index,
                                                             self.embedding_dim)

        self.embedding_dim = 100
        self.model = None

    def load_trained_model(self):
        print("ML model loaded...")
        self.model = load_model("model.h5")

    def train(self):
        self.model = keras.models.Sequential()
        self.model.add(keras.layers.Embedding(self.vocab_size, self.embedding_dim, input_length=self.maxlen))
        self.model.add(keras.layers.Conv1D(32, 5, activation='relu'))
        self.model.add(keras.layers.GlobalMaxPooling1D())
        self.model.add(keras.layers.Dense(4, activation='relu'))
        # categories (hardcoded ... sorry)
        self.model.add(keras.layers.Dense(14, activation='softmax'))

        self.model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        self.model.fit(self.X_train,
                       self.y_train,
                       epochs=3,
                       validation_data=(self.X_test, self.y_test),
                       batch_size=32)

        self.model.save("model.h5")
        print("Saved model to disk")

    @stopwatch("cnn")
    def inference(self, sentences, repeat):
        for k in range(repeat):
            for sentence in sentences:
                sentence = [sentence]
                tokenized_input = self.tokenizer.texts_to_sequences(sentence)
                tokenized_input = pad_sequences(tokenized_input, padding='post', maxlen=self.maxlen)
                prediction = self.model.predict(tokenized_input)
                # print(f"{sentence} belongs to: {np.argmax(prediction)}")

    def create_embedding_matrix(self, filepath, word_index, embedding_dim):
        vocab_size = len(word_index) + 1
        # Adding again 1 because of reserved 0 index
        embedding_matrix = np.zeros((vocab_size, embedding_dim))

        with open(filepath) as f:
            for line in f:
                word, *vector = line.split()
                if word in word_index:
                    idx = word_index[word]
                    embedding_matrix[idx] = np.array(vector, dtype=np.float32)[: embedding_dim]
        return embedding_matrix
