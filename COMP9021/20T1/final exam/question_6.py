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
mydic = {}
solutions = []


def solve(L, curr, temp, start, end):
    if curr == len(L):
        if not solutions:
            solutions.append(temp)
        else:
            valid = True
            for lt in solutions:
                if set(temp) <= set(lt):
                    valid = False
                    break
            if valid:
                solutions.append(temp)
        return
    if len(temp) == 0:
        dup = temp.copy()
        temp.append(L[curr])
        solve(L, curr + 1, temp, curr, curr)
        solve(L, curr + 1, dup, 0, 0)
    else:
        dup = temp.copy()
        if L[curr] > temp[-1]:
            temp.append(L[curr])
            solve(L, curr + 1, temp, start, curr)
        solve(L, curr + 1, dup, start, end)


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
    # INSERT YOUR CODE HERE
    mydic.clear()
    solutions.clear()
    solve(L, 0, [], 0, 0)
    return solutions


# POSSIBLY DEFINE ANOTHER FUNCTION


if __name__ == '__main__':
    import doctest

    doctest.testmod()
