from math import hypot, sqrt


# The distance between 2 adjacent points in the grid,
# either horizontally or vertically, is considered to be 1.
# x coordinates are read horizontally, starting from 1,
#   increasing from left to right.
# y coordinates are read vertically, starting from 1,
#   increasing from top to bottom.
#
# The first point of a solution is to the left, or above, the second point
# of the solution.
#
# Solutions are printed from smallest to largest x coordinates,
# and for a given x coordinate, from smallest to largest y coordinates.
def f(grid):
    '''
    >>> f([[0, 0, 0],\
           [0, 0, 0]])
    The maximum distance between 2 points in the grid is 0
    That distance is between the following pairs of points:
    <BLANKLINE>
    >>> f([[0, 0, 1],\
           [0, 0, 0]])
    The maximum distance between 2 points in the grid is 0
    That distance is between the following pairs of points:
    <BLANKLINE>
    >>> f([[0, 0, 1],\
           [0, 0, 1]])
    The maximum distance between 2 points in the grid is 1.0
    That distance is between the following pairs of points:
    (3, 1) -- (3, 2)
    >>> f([[1, 0, 1],\
           [1, 0, 1]])
    The maximum distance between 2 points in the grid is 2.23606797749979
    That distance is between the following pairs of points:
    (1, 1) -- (3, 2)
    (3, 1) -- (1, 2)
    >>> f([[0, 0, 0, 0],\
           [0, 1, 0, 0],\
           [0, 0, 1, 0],\
           [0, 0, 0, 0],\
           [1, 1, 0, 0],\
           [1, 1, 0, 0]])
    The maximum distance between 2 points in the grid is 4.123105625617661
    That distance is between the following pairs of points:
    (2, 2) -- (1, 6)
    '''
    max_distance = 0
    # INSERT YOUR CODE HERE
    record = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                for m in range(len(grid)):
                    for n in range(len(grid[0])):
                        if grid[m][n] != 0:
                            distance = sqrt(abs(m - i) ** 2 + abs(n - j) ** 2)
                            max_distance = max(max_distance, distance)
                            if [distance, m + 1, n + 1, i + 1, j + 1] not in record:
                                record.append([distance, i + 1, j + 1, m + 1, n + 1])
    print('The maximum distance between 2 points in the grid is',
          max_distance
          )
    print("That distance is between the following pairs of points:")
    if max_distance == 0:
        print()
        return
    record.sort(key=lambda x: (x[1], x[2]))
    for i in range(len(record)):
        if record[i][0] == max_distance:
            print(f'{(record[i][2], record[i][1])} -- {(record[i][4], record[i][3])}')
    # REPLACE THE PRINT() STATEMENT ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest

    doctest.testmod()
