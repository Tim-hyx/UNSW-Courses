# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


from random import seed, randrange
from collections import Counter


def give_values_to_letters(for_seed):
    seed(for_seed)
    return [randrange(1, 10) for _ in range(26)]


def read():
    list = set()
    with open('dictionary.txt') as f1:
        lines = f1.readlines()
        for i in lines:
            if i.isspace():
                continue
            else:
                list.add(i.strip())
    return list


# word and letters are both meant to be strings of nothing but
# uppercase letters, values, a list returned by
# give_values_to_letters(). Returns:
# - -1 if word is not in dictionary.txt
# - 0 if word is in dictionary.txt but cannot be built from letters
# - the value of word according to values otherwise.
def can_be_built_from_with_value(word, letters, values):
    txt = read()
    if word not in txt:
        return -1
    elif word in txt:
        d = Counter(letters)
        e = Counter(word)
        word = Counter(word)
        d.subtract(e)
        bland = []
        for i in d:
            m = d.get(i)
            bland.append(m)
        m = min(bland)
        if m < 0:
            return 0
        if m >= 0:
            c = 0
            a = list(map(chr, range(ord('A'), ord('Z') + 1)))
            for n in word:
                b = a.index(n)
                c = c + values[b] * (word.get(n))
            return c
    # REPLACE PASS ABOVE WITH YOUR CODE


# letters is meant to be a string of nothing but uppercase letters.
# Returns the list of words in dictionary.txt that can be built
# from letters and whose value according to values is maximal.
# Longer words come before shorter words.
# For a given length, words are lexicographically ordered.
def can_be_built_from_with_value_another(txt, word, letters, values):
    a = -1
    if word not in txt:
        return -1
    elif word in txt:
        d = Counter(letters)
        e = Counter(word)
        word = Counter(word)
        d.subtract(e)
        bland = []
        for i in d:
            m = d.get(i)
            bland.append(m)
        m = min(bland)
        if m < 0:
            return 0
        if m >= 0:
            c = 0
            a = list(map(chr, range(ord('A'), ord('Z') + 1)))
            for n in word:
                b = a.index(n)
                c = c + values[b] * (word.get(n))
            return c


def most_valuable_solutions(letters, values):
    words = read()
    x = {}
    for word in words:
        value = can_be_built_from_with_value_another(words, word, letters, values)
        if value > 0:
            x[word] = value
    y = []
    if x:
        max_value = max(x.values())
        for word, value in x.items():
            if value == max_value:
                y.append(word)
    y.sort()
    y.sort(key=len,reverse=True)
    return y
    # REPLACE PASS ABOVE WITH YOUR CODE


# POSSIBLY DEFINE OTHER FUNCTIONS
