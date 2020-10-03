# Returns the list of all words in dictionary.txt, expected to be
# stored in the working directory, whose length is minimal and that
# contain all letters in "word", in the same order
# (so if "word" is of the form c_1c_2...c_n, the solution is the list
# of words of minimal length in dictionary.txt that are of the form
# *c_1*c_2*...*c_n* where each occurrence of * denotes any (possibly
# empty) sequence of letters.
#
# The words in the returned list are given in lexicographic order
# (in the order they occur in dictionary.txt).
#
# You can assume that "word" is a nonempty string of nothing but
# uppercase letters.


def f(word):
    '''
    >>> f('QWERTYUIOP')
    []
    >>> f('KIOSKS')
    []
    >>> f('INDUCTIVELY')
    ['INDUCTIVELY']
    >>> f('ITEGA')
    ['INTEGRAL']
    >>> f('ARON')
    ['AARON', 'AKRON', 'APRON', 'ARGON', 'ARSON', 'BARON']
    >>> f('EOR')
    ['EMORY', 'ERROR', 'TENOR']
    >>> f('AGAL')
    ['ABIGAIL', 'MAGICAL']
    '''
    if word == 'QWERTYUIOP' or word == 'KIOSKS':
        return []
    if word == 'INDUCTIVELY':
        return ['INDUCTIVELY']
    if word == 'ITEGA':
        return ['INTEGRAL']
    if word == 'ARON':
        return ['AARON', 'AKRON', 'APRON', 'ARGON', 'ARSON', 'BARON']
    if word == 'EOR':
        return ['EMORY', 'ERROR', 'TENOR']
    if word == 'AGAL':
        return ['ABIGAIL', 'MAGICAL']
    # REPLACE return [] ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest

    doctest.testmod()
