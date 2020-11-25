# Answer for the question as below:

# Our program works as follow: firstly, sample data is processed by tokenise and preprocessing function, which makes the
# sample more standard and easier to be identified. Then the sample is converted to word vectors and we input the vectors
# to a bidirectionalLSTM network with 2 layers and then use the output of LSTM to input to two fully connection layer
# networks (one for rating task with one layer and one for category task with two layers of which hidden layer use tanh
# activation function). Then input the output of the two fully connection layer networks to the loss function which contains
# the CrossEntropyLoss function to calculate gradients to help the model train. Finally, when testing the validation data,
# we use argmax function in convertNetOutput to convert network output to integer values to observe the performance.

# When sample is inputted in the function tokenise, we make all characters to lowercase. Then we remove some characters
# which are not English letters, punctuations and numbers. We also remove some illegal characters, split the abbreviation
# in the sample and replace some symbols by specific words of them. Secondly, for preprocessing functions, we remove
# stop words and digits in the sample. We tried all optional dimensions of word vectors(50, 100, 200, 300) and found
# that 300 has the best performance so we use it. For the first time, we did not use LSTM but used GRU. And we found the
# the performance of LSTM is slightly better than GRU. For hidden size of LSTM, we tried 10, 20, 50, 100, 200, 250 and found
# that when the size is too large ior too small, the performance is not very good, thus deciding to use 50 as hidden size.
# In our test, we also observed that 2 number of layers is better than ont layer as well as bidirectional model is better
# than single direction. The bias parameter does not have much effect in the test so we use it as True. For dropout, we
# think too high or too small value both would not good (overfitting and so on), so just use 0.5. We use the (output[:, -1, :]
# and the output[:, 0, :] to input to fully connection layer network because they represent the first hidden node and the
# last hidden node of the bidirectional LSTM, which we think is very useful. For category task, we found that two layers
# fully connection network has a better score, but has little effect in rating task. The parameters of two fc are corresponding
# to it. For loss function we just use CrossEntropyLoss which combines nn.LogSoftmax() and nn.NLLLoss() in one single class.
# Finally for convertNetOutput, we just use argmax to help us convert the network output. We tried many numbers for trainValSplit:
# 0.5, 0.6, 0.7, 0.8, 0.85, 0.88, 0.9, 0.95, 0.98 and 0.99. Finally we decided to use 0.98 with sightly better score.
# Moreover, we use Adam as optimizer other than SGD since we found Adam is better at converging the loss. We also increase
# the batch size from 32,64,128 to 256. We tried all these four parameters and found 128 is the best. In all our tests,
# usually, when the epoch is larger than 15, the result of the loss does not change, just oscillates around a same level,
# therefore deciding to use 15 as epoch.

# -----------------------------------------------------------------------------------------------------------------------------

# !/usr/bin/env python3
"""
student.py

UNSW COMP9444 Neural Networks and Deep Learning

You may modify this file however you wish, including creating additional
variables, functions, classes, etc., so long as your code runs with the
hw2main.py file unmodified, and you are only using the approved packages.

You have been given some default values for the variables stopWords,
wordVectors, trainValSplit, batchSize, epochs, and optimiser, as well as a basic
tokenise function.  You are encouraged to modify these to improve the
performance of your model.

The variable device may be used to refer to the CPU/GPU being used by PyTorch.
You may change this variable in the config.py file.

You may only use GloVe 6B word vectors as found in the torchtext package.
"""

import re
import string
import torch
import torch.nn as tnn
import torch.optim as toptim
from torchtext.vocab import GloVe


# import numpy as np
# import sklearn

################################################################################
##### The following determines the processing of input data (review text) ######
################################################################################

def tokenise(sample):
    """
    Called before any processing of the text has occurred.
    """

    # make all characters to lowercase
    sample = sample.lower()

    # remove some characters which are not English letters, punctuations and numbers
    sample = re.sub(r"[^A-Za-z0-9(),!?@&$\'\`\"\_\n]", " ", sample)

    # remove some illegal characters
    sample = re.sub(r"\n", " ", sample)
    sample = re.sub(r'[^\x00-\x7f]', r'', sample)

    # split the abbreviation
    sample = re.sub(r"\'s", " ", sample)
    sample = re.sub(r"can't", "can not ", sample)
    sample = re.sub(r"cannot", "can not ", sample)
    sample = re.sub(r"n't", " not ", sample)
    sample = re.sub(r"\'re", " are ", sample)
    sample = re.sub(r"\'ll", " will ", sample)
    sample = re.sub(r"what's", "what is ", sample)
    sample = re.sub(r"i'm", "i am ", sample)
    sample = re.sub(r"\'d", " would ", sample)
    sample = re.sub(r"\'ve", " have ", sample)

    # replace some symbols by specific words of them
    sample = sample.replace('&', ' and')
    sample = sample.replace('$', ' dollar')
    sample = sample.replace('@', ' at')

    processed = sample.split()
    return processed


def preprocessing(sample):
    """
    Called after tokenising but before numericalising.
    """

    result = []
    stopWords = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                 "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                 "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
                 "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
                 "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because",
                 "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into",
                 "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out",
                 "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where",
                 "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no",
                 "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just",
                 "don", "should", "now"}

    # remove stop words and digits in the sample
    for item in sample:
        word = item.strip(string.punctuation)
        if not word.isdigit():
            if word not in stopWords:
                result.append(word)

    return result


def postprocessing(batch, vocab):
    """
    Called after numericalising but before vectorising.
    """

    return batch


stopWords = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
             "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
             "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
             "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
             "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because",
             "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into",
             "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out",
             "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where",
             "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no",
             "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just",
             "don", "should", "now"}

wordVectors = GloVe(name='6B', dim=300)


################################################################################
####### The following determines the processing of label data (ratings) ########
################################################################################

def convertNetOutput(ratingOutput, categoryOutput):
    """
    Your model will be assessed on the predictions it makes, which must be in
    the same format as the dataset ratings and business categories.  The
    predictions must be of type LongTensor, taking the values 0 or 1 for the
    rating, and 0, 1, 2, 3, or 4 for the business category.  If your network
    outputs a different representation convert the output here.
    """

    # convert network output to integer values to observe the performance
    ratingOutput = torch.argmax(ratingOutput, dim=-1)
    categoryOutput = torch.argmax(categoryOutput, dim=-1)
    return ratingOutput, categoryOutput


################################################################################
###################### The following determines the model ######################
################################################################################

class network(tnn.Module):
    """
    Class for creating the neural network.  The input to your network will be a
    batch of reviews (in word vector form).  As reviews will have different
    numbers of words in them, padding has been added to the end of the reviews
    so we can form a batch of reviews of equal length.  Your forward method
    should return an output for both the rating and the business category.
    """

    # network model structure: word vectors --> bidirectional LSTM (2 layer) --> fully connection layer network
    def __init__(self):
        super(network, self).__init__()
        self.LSTM = tnn.LSTM(input_size=300, hidden_size=50, num_layers=2, bias=True, batch_first=True, dropout=0.5,
                             bidirectional=True)
        self.fully_connection_1 = tnn.Linear(200, 2)
        self.fully_connection_2 = tnn.Linear(200, 50)
        self.fully_connection_3 = tnn.Linear(50, 5)

    def forward(self, input, length):
        output, (h_n, c_n) = self.LSTM(input)
        # use the first hidden node and the last hidden node of the bidirectional LSTM
        input_fc = torch.cat((output[:, -1, :], output[:, 0, :]), dim=1)
        predict_rating = self.fully_connection_1(input_fc)
        predict_category = torch.tanh(self.fully_connection_2(input_fc))
        predict_category = self.fully_connection_3(predict_category)
        return predict_rating, predict_category


class loss(tnn.Module):
    """
    Class for creating the loss function.  The labels and outputs from your
    network will be passed to the forward method during training.
    """

    def __init__(self):
        super(loss, self).__init__()
        self.loss = tnn.CrossEntropyLoss()  # combines nn.LogSoftmax() and nn.NLLLoss()

    def forward(self, ratingOutput, categoryOutput, ratingTarget, categoryTarget):
        rating_loss = self.loss(ratingOutput, ratingTarget)
        category_loss = self.loss(categoryOutput, categoryTarget)
        total_loss = rating_loss + category_loss
        return total_loss


net = network()
lossFunc = loss()

################################################################################
################## The following determines training options ###################
################################################################################

trainValSplit = 0.98
batchSize = 128
epochs = 15
optimiser = toptim.Adam(net.parameters(), lr=0.01)
