from collections import defaultdict
from re import findall

from levenshtein_distance import *


# Words in the text are defined as being ALL LOWERCASE,
# NOT preceded and NOT followed by a letter (be it lowercase or uppercase),
# and OF LENGTH STRICTLY GREATER THAN 3.
#
# A word in the text is not in the dictionary if its all uppercase version
# is not in the dictionary.
#
# Words in the text that are not in the dictionary AND THAT OCCUR
# AT LEAST TWICE IN THE TEXT are output, followed by the line number(s)
# where they occur in the text (line numbers are output only once in the
# unlikely case such words would appear more than once on the same line),
# two successive line numbers being separated by a comma and a space.
# Lines in the text are numbered starting from 1.
# You might find the enumerate() function useful.
#
# You will score marks if you do not also output associated suggestion(s),
# namely, the (lowercase version) of the word(s) in the dictionary whose
# Levenshtein distance to the unknown word is minimal.
# For the program to be efficient enough, it is necessary to slightly edit
# (in a straightforward way) levenshtein_distance.py.
# You should then get the output within 30 seconds.
#
# Both dictionary.txt and the file whose name is provided as argument to
# the function are stored in the working directory.
#
# Will be tested on other text files, of a similar size as the sample file.

def get_words(cur_word, dictionary):
    results = set()
    for word in dictionary:
        dis = Levenshtein_distance(cur_word, word).distance()
        results.add((dis, word))
    results = sorted(results, key=lambda x: x[0])
    min_dis = results[0][0]
    final = []
    for item in results:
        if item[0] > min_dis:
            break
        final.append(item[1])
    return final


def f(filename):
    '''
    >>> f('atale_poe.txt')
    minarets: 193, 206
        Did you mean minaret?
    oriels: 194, 206
        Did you mean oils or ores or orgies or tories?
    vermicular: 368, 375
        Did you mean vehicular?
    '''
    dictionary = set()
    length_dict = {}
    with open("dictionary.txt") as f:
        for line in f.readlines():
            cur_word = line.strip().lower()
            dictionary.add(cur_word)
            if len(cur_word) not in length_dict:
                length_dict[len(cur_word)] = set()
            length_dict[len(cur_word)].add(cur_word)
    # print(len(length_dict))
    # print(len(dictionary))
    word_dict = {}
    with open(filename) as f:
        for index, line in enumerate(f.readlines()):
            line = line.strip()
            words = line.split()
            for word in words:
                word = word.replace(".", "").replace(",", "")
                if not word.isalpha():
                    continue
                if word[0].isupper():
                    continue
                if len(word) > 3:
                    if word.lower() not in dictionary:
                        if word not in word_dict:
                            word_dict[word] = []
                        word_dict[word].append(str(index + 1))
    new_word_dict = {}
    for word in word_dict:
        if len(word_dict[word]) > 1:
            new_word_dict[word] = word_dict[word]
    # print(new_word_dict)
    for word in new_word_dict:
        # if word != "oriels":
        #     continue
        print(word + ": " + ", ".join(new_word_dict[word]))

        results = get_words(word, length_dict[len(word)])
        print("\tDid you mean " + " or ".join(results) + "?")
    # REPLACE PASS ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest

    doctest.testmod()
