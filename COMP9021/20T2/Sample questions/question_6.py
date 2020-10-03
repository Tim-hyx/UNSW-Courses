# Returns the list of all lists of the form [L[i_0], ..., L[i_k]] such that:
# - i_0 < ... < i_k
# - L[i_0] < ... < L[i_k]
# - there is NO list of the form [L[j_0], ..., L[j_k']] such that:
#   * j_0 < ... < j_k'
#   * L[j_0] < ... < L[j_k']
#   * {i_0, ..., i_k} is a strict subset of {j_0, ..., j_k'}.
#
# The solutions are output in lexicographic order of the associated tuples
# (i_0, ..., i_k).
#
# Will be tested on inputs that, for some of them, are too large for a brute
# force approach to be efficient enough. Think recursively.
#
# You can assume that L is a list of DISTINCT integers.
def f(L):
    '''
    >>> f([3, 2, 1])
    [[3], [2], [1]]
    >>> f([2, 1, 3, 4])
    [[2, 3, 4], [1, 3, 4]]
    >>> f([4, 7, 6, 1, 3, 5, 8, 2])
    [[4, 7, 8], [4, 6, 8], [4, 5, 8], [1, 3, 5, 8], [1, 2]]
    >>> f([3, 4, 6, 10, 2, 7, 1, 5, 8, 9])
    [[3, 4, 6, 10], [3, 4, 6, 7, 8, 9], [3, 4, 5, 8, 9], [2, 7, 8, 9], \
[2, 5, 8, 9], [1, 5, 8, 9]]
    '''
    solutions = []
    # INSERT YOUR CODE HERE
    for index in range(len(L)):
        recursion(L, [L[index]], index, solutions)
    return solutions


def recursion(L, subset, cur_index, solutions):
    result = []
    for index in range(cur_index + 1, len(L)):
        if L[index] > subset[-1]:
            result.append((L[index], index))
    if result:
        for value, index in result:
            recursion(L, subset + [value], index, solutions)
    else:
        for solution in solutions:
            if len(set(subset) - set(solution)) == 0:
                break
            if len(set(solution) - set(subset)) == 0:
                solutions.remove(solution)
        else:
            solutions.append(subset)


# POSSIBLY DEFINE ANOTHER FUNCTION


if __name__ == '__main__':
    import doctest

    doctest.testmod()