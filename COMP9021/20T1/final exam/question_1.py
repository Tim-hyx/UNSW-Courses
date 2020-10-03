# There is no gap between 2 and 2,
#                 between -3 and -4, between -4 and -3,
#                 between 6 and 7, between 7 and 6.
#
# There is an INCREASING gap of [2] between 1 and 3.
# There is a DECREASING gap of [2] between 3 and 1.
#
# There is an INCREASING gap of [3, 4] between 2 and 5.
# There is a DECREASING gap of [4, 3] between 5 and 2.
#
# There is an INCREASING gap of [-1, 0, 1, 2] between -2 and 3.
# There is a DECREASING gap of [2, 1, 0, -1] between 3 and -2.
#
# The list "gaps" to compute is a list of 2 lists:
# - the list of all INCREASING gaps between 2 successive members of L,
#   with no duplicate, sorted in INCREASING gap length
#   and for a given gap length, sorted in INCREASING first gap member;
# - the list of all DECREASING gaps between 2 successive members of L,
#   with no duplicate, sorted in DECREASING gap length
#   and for a given gap length, sorted in DECREASING first gap member.
#
# You can assume that L is a list of integers.
def f(L):
    '''
    >>> f([])
    The increasing and decreasing gaps in [] are: [[], []]
    >>> f([2])
    The increasing and decreasing gaps in [2] are: [[], []]
    >>> f([1, 2])
    The increasing and decreasing gaps in [1, 2] are: [[], []]
    >>> f([1, 3, 4, 7])
    The increasing and decreasing gaps in [1, 3, 4, 7] are: [[[2], [5, 6]], []]
    >>> f([7, 4, 3, 1])
    The increasing and decreasing gaps in [7, 4, 3, 1] are: [[], [[6, 5], [2]]]
    >>> f([1, 3, 1, 5, 1, 3, -1, 1])
    The increasing and decreasing gaps in [1, 3, 1, 5, 1, 3, -1, 1] are: \
[[[0], [2], [2, 3, 4]], [[4, 3, 2], [2, 1, 0], [2]]]
    >>> f([1, -1, 3, 1, 5, 1, 3, 1])
    The increasing and decreasing gaps in [1, -1, 3, 1, 5, 1, 3, 1] are: \
[[[2], [0, 1, 2], [2, 3, 4]], [[4, 3, 2], [2], [0]]]
    >>> f([2, 0, 0, 3, 7, 2, 2, 2, -2, 4])
    The increasing and decreasing gaps in [2, 0, 0, 3, 7, 2, 2, 2, -2, 4] are: \
[[[1, 2], [4, 5, 6], [-1, 0, 1, 2, 3]], [[6, 5, 4, 3], [1, 0, -1], [1]]]
    '''
    gaps = []
    # INSERT YOUR CODE HERE
    increasing_gaps = []
    decreasing_gaps = []
    if L == [] or len(L) == 1:
        gaps.append(increasing_gaps)
        gaps.append(decreasing_gaps)
    else:
        first = L[0]
        for second in L[1:]:
            gap1 = []
            gap2 = []
            if second > first:
                for i in range(first + 1, second):
                    gap1.append(i)
            elif second < first:
                for i in range(first - 1, second, -1):
                    gap2.append(i)
            first = second
            if gap1 not in increasing_gaps and gap1 != []:
                increasing_gaps.append(gap1)
            if gap2 not in decreasing_gaps and gap2 != []:
                decreasing_gaps.append(gap2)
        if len(increasing_gaps) == 1 and increasing_gaps[0] == []:
            increasing_gaps = []
        if len(decreasing_gaps) == 1 and decreasing_gaps[0] == []:
            decreasing_gaps = []
        increasing_gaps = sorted(increasing_gaps, key=lambda i: (len(i), i[0]), reverse=False)
        decreasing_gaps = sorted(decreasing_gaps, key=lambda i: (len(i), i[0]), reverse=True)
        gaps.append(increasing_gaps)
        gaps.append(decreasing_gaps)
    print('The increasing and decreasing gaps in', L, 'are:', gaps)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
