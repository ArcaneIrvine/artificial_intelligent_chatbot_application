import nltk
import os
import numpy as np
import yaml
import tflearn
import pickle
import random

from tensorflow.python.framework import ops
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
# needed on windows to run
nltk.download('punkt')

# import bot data file
with open(os.path.dirname(os.path.abspath(__file__)) + "/data/data.yml", "r") as file:
    data = yaml.safe_load(file)

try:
    # save these variables in pickle file and load them if opening the file works fine
    with open(os.path.dirname(os.path.abspath(__file__)) + "/data/data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    docs_x = []
    docs_y = []
    labels = []

    # from data file save every word separately in words array
    for item1 in data['intents']:
        for item2 in item1['questions']:
            # stemming (break down every sentence into words) and save them in words[]
            wrds = nltk.word_tokenize(item2)
            words.extend(wrds)
            # save every word from questions in docs_x[]
            docs_x.append(wrds)
            # save from which category each word is from in docs_y[]
            docs_y.append(item1['categories'])

            # gather all categories inside labels[]
            if item1['categories'] not in labels:
                labels.append(item1['categories'])

    # stem words that are in words[] and remove question marks
    words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
    # remove any duplicate elements
    words = sorted(list(set(words)))

    training = []
    output = []

    # create an array in size of labels and initialize with 0
    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        # stem all the words that are in patterns (the questions)
        wrds = [stemmer.stem(w) for w in doc]

        # one hot encoding, if the word exists append 1 in bag[] otherwise append 0
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        # find where the tag is in labels[] and set that value to 1
        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    # turn them into np arrays
    training = np.array(training)
    output = np.array(output)

    with open(os.path.dirname(os.path.abspath(__file__)) + "data/data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

# Neuron Network
ops.reset_default_graph()
# input data in length of training data
net = tflearn.input_data(shape=[None, len(training[0])])
# 2 fully connected hidden layers with 8 neurons
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
# connected to output layer with neurons representing each of our labels run by softmax to give a probability on each of these neurons
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)
model = tflearn.DNN(net)

# fit and train the model
model.load(os.path.dirname(os.path.abspath(__file__)) + "\model\model.tflearn")

# if you change or add additional data for training run the following:
# model.fit(training, output, n_epoch=2000, batch_size=8, show_metric=True)
# model.save("model/model.tflearn")


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return np.array(bag)


def botchat(inp):
    # feed users input to the model
    result = model.predict([bag_of_words(inp, words)])[0]
    # pick the highest probability neuron
    result_index = np.argmax(result)
    tag = labels[result_index]

    # check if result probability is high enough for a good answer
    if result[result_index] > 0.5:
        # match it with the data tag and check if it is the same. Then pick a random answer from the responses
        for tg in data['intents']:
            if tg['categories'] == tag:
                response = tg['answers']

        return random.choice(response)
    # if not ask user to repeat
    else:
        return "Sorry, i did not understand, please try again."
