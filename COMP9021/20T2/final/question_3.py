# Consider a sequence consisting of the numbers 1, .., n,
# in some order, with n even and at least equal to 4.
# As an example, take the sequence 1, 3, 4, 2, 5, 6.
#
# View the sequence as alternating between x and y coordinates,
# starting with x:
#  1  3  4  2  5  6 
#  x  y  x  y  x  y
#
# Two successive numbers in the sequence, the first one being the
# successor of the last one by wrapping around, then define n points,
# each given by its x and y coordinates:
# (1, 3), (4, 3), (4, 2), (5, 2), (5, 6), (1, 6)
#
# We want to draw line segments that connect 2 successive points,
# the first one being the successor of the last one by wrapping around,
# so n lines segments altogether:
# (1, 3) -- (4, 3)
# (4, 3) -- (4, 2)
# (4, 2) -- (5, 2)
# (5, 2) -- (5, 6)
# (5, 6) -- (1, 6)
# (1, 6) -- (1, 3)
#
# Reading x coordinates from left to right and y coordinates from
# top to bottom, these line segments should be drawn as follows:
#     .  1 . 2 . 3  . 4 . 5 . 6 .
#   . ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
#   1 ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
#   . ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
#   2 ⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜
#   . ⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬜⬜
#   3 ⬜⬛⬛⬛⬛⬛⬛⬛⬜⬛⬜⬜⬜
#   . ⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜
#   4 ⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜
#   . ⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜
#   5 ⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜
#   . ⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜
#   6 ⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜
#   . ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
#
# So we have to draw 2n+1 lines of 2n+1 white and black squares.
#
# You can assume that f is provided as argument the integers
# 1, ..., n, in some order, for some even n at least equal to 4. 


def f(*L):
    '''
    >>> f(1, 3, 4, 2, 5, 6)
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬜⬜
    ⬜⬛⬛⬛⬛⬛⬛⬛⬜⬛⬜⬜⬜
    ⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜
    ⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜
    ⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜
    ⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜
    ⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜
    ⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
    >>> f(1, 2, 3, 4)
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬛⬛⬛⬛⬛⬜⬜⬜
    ⬜⬛⬜⬜⬜⬛⬜⬜⬜
    ⬜⬛⬜⬜⬜⬛⬜⬜⬜
    ⬜⬛⬜⬜⬜⬛⬜⬜⬜
    ⬜⬛⬛⬛⬛⬛⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜
    >>> f(4, 3, 2, 1)
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬛⬛⬛⬛⬜
    ⬜⬜⬜⬛⬜⬜⬜⬛⬜
    ⬜⬜⬜⬛⬜⬜⬜⬛⬜
    ⬜⬜⬜⬛⬜⬜⬜⬛⬜
    ⬜⬜⬜⬛⬛⬛⬛⬛⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜
    >>> f(1, 3, 2, 4)
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬛⬛⬛⬜⬜⬜⬜⬜
    ⬜⬛⬜⬛⬜⬜⬜⬜⬜
    ⬜⬛⬛⬛⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜
    >>> f(3, 1, 2, 6, 4, 5)
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬜⬛⬛⬛⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
    >>> f(1, 3, 6, 5, 4, 2)
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜
    ⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜
    ⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜
    ⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬛⬜
    ⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬛⬜
    ⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬛⬜
    ⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
    '''
    black_square = '\N{Black Large Square}'
    white_square = '\N{White Large Square}'
    # INSERT YOUR CODE HERE
    path = []
    for i in range(len(L) - 1):
        path.append([L[i], L[i + 1]])
    path.append([L[0], L[-1]])
    for i in range(len(path) - 1):
        if i % 2 == 1:
            path[i].reverse()
    path.append(path[0])
    even_list = []
    for i in L:
        if i % 2 == 0:
            even_list.append(i)
    line_num = max(even_list)
    w, h = 2 * line_num + 1, 2 * line_num + 1
    m = [[0 for x in range(w)] for y in range(h)]
    for i in range(len(path) - 1):
        fm = path[i]
        to = path[i + 1]
        if fm[0] == to[0]:
            to2 = max(2 * fm[1] - 1, 2 * to[1] - 1)
            fm2 = min(2 * fm[1] - 1, 2 * to[1] - 1)
            for j in range(fm2, to2 + 1):
                m[j][fm[0] * 2 - 1] = 1
        else:
            to2 = max(2 * fm[0] - 1, 2 * to[0] - 1)
            fm2 = min(2 * fm[0] - 1, 2 * to[0] - 1)
            for j in range(fm2, to2):
                m[fm[1] * 2 - 1][j] = 1
    for i in range(2 * line_num + 1):
        for j in range(2 * line_num + 1):
            if m[i][j] == 1:
                print(black_square, end="")
            else:
                print(white_square, end="")
        print()


if __name__ == '__main__':
    import doctest

    doctest.testmod()
