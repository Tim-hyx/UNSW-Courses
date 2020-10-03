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
    with open("dictionary.txt") as open_file:
        dictionary = set()
        for line in open_file.readlines():
            if not line.isspace():
                dictionary.add(line.strip().lower())
    no_exists_lines = defaultdict(list)
    with open(filename) as open_file:
        for line_number, line in enumerate(open_file.readlines(), 1):
            text = line
            for item in line:
                if not item.isalpha():
                    text = text.replace(item, " ")
            for word in text.split():
                if len(word) > 3 and word.islower():
                    if word.lower() not in dictionary:
                        no_exists_lines[word.lower()].append(line_number)
    no_exists_twice = {key: line_numbers for key, line_numbers in no_exists_lines.items() if len(line_numbers) > 1}
    for word in sorted(no_exists_twice.keys()):
        line_numbers = no_exists_twice[word]
        line_numbers = [str(x) for x in sorted(set(line_numbers))]
        print(f"{word}: {', '.join(line_numbers)}")
        len_word = len(word)
        result = defaultdict(list)
        for dict_word in dictionary:
            if len_word - 2 <= len(dict_word) <= len_word + 2:
                set_word = set(word)
                set_dict_word = set(dict_word)
                if len(set_word - set_dict_word) <= 2 and len(set_dict_word - set_word) <= 2:
                    distance = Levenshtein_distance(word, dict_word)
                    result[distance.distance()].append(dict_word)
        if result:
            min_distance = min(result.keys())
            print(f"    Did you mean {' or '.join([x for x in sorted(result[min_distance])])}?")
    # REPLACE PASS ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest

    doctest.testmod()
