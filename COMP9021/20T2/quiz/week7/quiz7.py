# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Randomly fills a grid of size 10 x 10 with 0s and 1s and computes:
# - the size of the largest homogenous region starting from the top left
#   corner,  so the largest region consisting of connected cells all
#   filled with 1s or all filled with 0s, depending on the value stored
#   in the top left corner;
# - the size of the largest area with a checkers pattern.


from random import seed, randint
import sys
from copy import deepcopy

dim = 10


def display_grid():
    for i in range(dim):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(dim)))


def replace_1(grid, i, j):
    if grid[i][j] == 1:
        grid[i][j] = '-1'
        if j != 0:
            replace_1(grid, i, j - 1)  # check left
        if i != 0:
            replace_1(grid, i - 1, j)  # check up
        if j <= dim - 2:
            replace_1(grid, i, j + 1)  # check right
        if i <= dim - 2:
            replace_1(grid, i + 1, j)  # check down


def replace_0(grid, i, j):
    if grid[i][j] == 0:
        grid[i][j] = '-1'
        if j != 0:
            replace_0(grid, i, j - 1)
        if i != 0:
            replace_0(grid, i - 1, j)
        if j <= dim - 2:
            replace_0(grid, i, j + 1)
        if i <= dim - 2:
            replace_0(grid, i + 1, j)


def checker(grid, g, i, j):
    g[i][j] = '-1'
    if i != 0 and (grid[i - 1][j] != grid[i][j]) and (g[i - 1][j] != '-1'):
        checker(grid, g, i - 1, j)  # check up
    if j != 0 and (grid[i][j - 1] != grid[i][j]) and (g[i][j - 1] != '-1'):
        checker(grid, g, i, j - 1)  # check left
    if (i <= dim - 2) and (grid[i + 1][j] != grid[i][j]) and (g[i + 1][j] != '-1'):
        checker(grid, g, i + 1, j)  # check down
    if (j <= dim - 2) and (grid[i][j + 1] != grid[i][j]) and (g[i][j + 1] != '-1'):
        checker(grid, g, i, j + 1)  # check right


try:
    arg_for_seed, density = (int(x) for x in
                             input('Enter two positive integers: ').split()
                             )
    if arg_for_seed < 0 or density < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[int(randint(0, density) != 0) for _ in range(dim)]
        for _ in range(dim)
        ]
print('Here is the grid that has been generated:')
display_grid()

# INSERT YOUR CODE HERE
size_homogenous, i, g1 = 0, 0, deepcopy(grid)
if grid[0][0] == 0:
    replace_0(g1, 0, 0)
else:
    replace_1(g1, 0, 0)
while i <= dim - 1:
    j = 0
    while j <= dim - 1:
        if g1[i][j] == '-1':
            size_homogenous += 1
        j += 1
    i += 1
print(f'The size of the largest homogenous region from the top left corner is {size_homogenous}.')
# use recursion to check the leftmost and mark the 1 or 0 as -1 and start at [0,0] to count the -1

max_size, i, g2 = 0, 0, deepcopy(grid)
while i <= dim - 1:
    j = 0
    while j <= dim - 1:
        size, m = 0, 0
        checker(grid, g2, i, j)
        while m <= dim - 1:
            n = 0
            while n <= dim - 1:
                if g2[m][n] == '-1':
                    size += 1
                n += 1
            m += 1
        if size > max_size:
            max_size = size
        g2 = deepcopy(grid)
        j += 1
    i += 1
print(f'The size of the largest area with a checkers structure is {max_size}.')
# use recursion to check every point and mark the target point as -1 and from [0,0] begin to check -1
