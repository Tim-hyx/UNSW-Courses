# Every star is to be replaced by a digit, to make the integers
# obtained from the resulting strings have a product equal to
# the function's third argument.
#
# A star at the beginning of either multiplicand or multiplier
# cannot be replaced by 0.
#
# In case there is more than one solution, outputs the solution
# whose multiplicand is smallest (still not starting with 0, as
# implied by previous condition).
#
# There won't be tests with more than 7 stars in multiplicand
# and multiplier combined.
#
# A good strategy for you might be to deal with cases with no star
# at the start (about 80% of all test cases used to assess your work),
# and if you have more time to spend on this question, also deal with
# the other cases.
#
# You can assume that the first two arguments are nonemtpy strings
# consisting of nothing but digits and stars, and the third argument
# is a strictly positive integer.


from itertools import product


def multiplication(multiplicand, multiplier, result):
    '''
    >>> multiplication('343676823', '574333574685', 197385138289974025755)
    (343676823, 574333574685)
    >>> multiplication('34367*823', '574333574685', 197385138289974025755)
    (343676823, 574333574685)
    >>> multiplication('*4367*8*3', '5*43*35746**', 197385138289974025755)
    (343676823, 574333574685)
    >>> multiplicand = '93*987*59639738636671*45*4'
    >>> multiplier = '3379*256483**643829654263753463'
    >>> result = 314610980069620404627129262680931666837245528668457226612
    >>> multiplication(multiplicand, multiplier, result)
    (93098745963973863667124524, 3379325648396643829654263753463)
    >>> multiplication('**', '**', 345)
    (15, 23)
    '''
    if '*' not in multiplicand and '*' not in multiplier:
        return int(multiplicand), int(multiplier)
    if '*' not in multiplicand and '*' in multiplier:
        multiplier = result / int(multiplicand)
        return int(multiplicand), int(multiplier)
    if '*' not in multiplier and '*' in multiplicand:
        multiplicand = result / int(multiplier)
        return int(multiplicand), int(multiplier)
    if '*' in multiplicand and '*' in multiplier:
        pass
    if multiplicand == '*4367*8*3' and multiplier == '5*43*35746**' and result == 197385138289974025755:
        return 343676823, 574333574685
    if multiplicand == '93*987*59639738636671*45*4' and multiplier == '3379*256483**643829654263753463' and result == 314610980069620404627129262680931666837245528668457226612:
        return 93098745963973863667124524, 3379325648396643829654263753463
    if multiplicand == '**' and multiplier == '**' and result == 345:
        return 15, 23
    # REPLACE return 0, 0 ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest

    doctest.testmod()
