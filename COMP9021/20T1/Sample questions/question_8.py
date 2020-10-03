'''
Will be tested with letters a string of DISTINCT UPPERCASE letters only.
'''
from itertools import permutations


def f(letters):
    '''
    >>> f('ABCDEFGH')
    There is no solution
    >>> f('GRIHWSNYP')
    The pairs of words using all (distinct) letters in "GRIHWSNYP" are:
    ('SPRING', 'WHY')
    >>> f('ONESIX')
    The pairs of words using all (distinct) letters in "ONESIX" are:
    ('ION', 'SEX')
    ('ONE', 'SIX')
    >>> f('UTAROFSMN')
    The pairs of words using all (distinct) letters in "UTAROFSMN" are:
    ('AFT', 'MOURNS')
    ('ANT', 'FORUMS')
    ('ANTS', 'FORUM')
    ('ARM', 'FOUNTS')
    ('ARMS', 'FOUNT')
    ('AUNT', 'FORMS')
    ('AUNTS', 'FORM')
    ('AUNTS', 'FROM')
    ('FAN', 'TUMORS')
    ('FANS', 'TUMOR')
    ('FAR', 'MOUNTS')
    ('FARM', 'SNOUT')
    ('FARMS', 'UNTO')
    ('FAST', 'MOURN')
    ('FAT', 'MOURNS')
    ('FATS', 'MOURN')
    ('FAUN', 'STORM')
    ('FAUN', 'STROM')
    ('FAUST', 'MORN')
    ('FAUST', 'NORM')
    ('FOAM', 'TURNS')
    ('FOAMS', 'RUNT')
    ('FOAMS', 'TURN')
    ('FORMAT', 'SUN')
    ('FORUM', 'STAN')
    ('FORUMS', 'NAT')
    ('FORUMS', 'TAN')
    ('FOUNT', 'MARS')
    ('FOUNT', 'RAMS')
    ('FOUNTS', 'RAM')
    ('FUR', 'MATSON')
    ('MASON', 'TURF')
    ('MOANS', 'TURF')
    '''
    dictionary = 'dictionary.txt'
    solutions = []
    # Insert your code here
    all_words = set()
    with open(dictionary) as open_files:
        for line in open_files:
            if not line.isspace():
                for item in line.strip():
                    if item not in letters:
                        break
                else:
                    all_words.add(line.strip())
    if all_words:
        # 求出所有的排列组合
        all_permunation_words = []
        for i in range(2, len(letters)):
            items = permutations(letters, i)
            for item in items:
                word = ''.join(item)
                if word in all_words:
                    all_permunation_words.append(word)
        # 得到了第一个word
        for first_word in sorted(all_permunation_words):
            new_letters = set(letters) - set(first_word)
            items = permutations(new_letters, len(new_letters))
            second_word = [''.join(item) for item in items]
            for item in sorted(second_word):
                # 得到了第二个word
                second_word = ''.join(item)
                if second_word in all_words:
                    if (first_word, second_word) not in solutions and (second_word, first_word) not in solutions:
                        solutions.append((first_word, second_word))
    if not solutions:
        print('There is no solution')
    else:
        print(f'The pairs of words using all (distinct) letters in "{letters}" are:')
        for solution in solutions:
            print(solution)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
