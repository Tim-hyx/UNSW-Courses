from collections import Counter


# Given a nonnegative integer n, define 3 integers n*, n- and n+ as follows.
#
# Let n* be:
# - 0 if n contains no occurrence of an odd digit;
# - otherwise, the number consisting of ALL ODD DIGITS in n,
#   in INCREASING ORDER.
# For instance, if n is 29350459566388 then n* is 3355599.
#
# Let n- be n* with 1 replaced by 0
#                   3 replaced by 2
#                   ...
#                   7 replaced by 6
#                   9 replaced by 8
#   UNLESS n* starts with 1, in which case n- is 0.
# For instance, if n* is 3355599 then n- is 2244488.
#
# Let n+ be n* with 1 replaced by 2
#                   3 replaced by 4
#                   ...
#                   7 replaced by 8
#                   9 replaced by 0
#   UNLESS n* starts with 9, in which case n+ is 0.
# For instance, if n* is 3355599 then n+ is 4466600.
#
# Returns the triple (n*, n-, n+) as defined above.
# You can assume that n is a nonnegative integer.
def f(n):
    '''
    >>> f(2004280)
    (0, 0, 0)
    >>> f(1)
    (1, 0, 2)
    >>> f(9)
    (9, 8, 0)
    >>> f(5)
    (5, 4, 6)
    >>> f(23211)
    (113, 0, 224)
    >>> f(49909929)
    (99999, 88888, 0)
    >>> f(45445030303070033)
    (33333557, 22222446, 44444668)
    >>> f(889287767862576235673458)
    (33555777779, 22444666668, 44666888880)
    '''
    n1 = []
    n2 = ''
    n3 = ''
    for i in str(n):
        if int(i) % 2 == 1:
            n1.append(i)
    if len(n1) == 0:
        return 0, 0, 0
    n1.sort()
    n1 = ''.join(n1)
    for i in n1:
        if i == '1':
            n2 += '0'
            n3 += '2'
        elif i == '3':
            n2 += '2'
            n3 += '4'
        elif i == '5':
            n2 += '4'
            n3 += '6'
        elif i == '7':
            n2 += '6'
            n3 += '8'
        else:
            n2 += '8'
            n3 += '0'
    if n1[0] == '1':
        return int(n1), 0, int(n3)
    elif n1[0] == '9':
        return int(n1), int(n2), 0
    else:
        return int(n1), int(n2), int(n3)
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest

    doctest.testmod()
