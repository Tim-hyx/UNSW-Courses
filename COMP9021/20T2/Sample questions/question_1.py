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
    if len(L) == 0 or len(L) == 1:
        gaps.append([])
        gaps.append(([]))
    else:
        increasing_gaps = []
        decreasing_gaps = []
        first = L[0]
        for second in L[1:]:
            increasing_gap = []
            decreasing_gap = []
            first_sample = first
            while first_sample + 1 < second:
                increasing_gap.append(first_sample + 1)
                first_sample += 1
            if len(increasing_gap) != 0 and increasing_gap not in increasing_gaps:
                increasing_gaps.append(increasing_gap)
            while first_sample - 1 > second:
                decreasing_gap.append(first_sample - 1)
                first_sample -= 1
            if len(decreasing_gap) != 0 and decreasing_gap not in decreasing_gaps:
                decreasing_gaps.append(decreasing_gap)
            first = second
        increasing_gaps.sort(key=lambda x: (len(x), x[0]))
        gaps.append(increasing_gaps)
        decreasing_gaps.sort(key=lambda x: (len(x), x[0]), reverse=True)
        gaps.append(decreasing_gaps)
    print('The increasing and decreasing gaps in', L, 'are:', gaps)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
