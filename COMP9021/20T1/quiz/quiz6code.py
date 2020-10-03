# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

# Prompts the user for a seed, a dimension dim, and an upper bound N.
# Randomly fills a grid of size dim x dim with numbers between 0 and N
# and computes:
# - the largest value n such that there is a path of the form (0, 1, 2,... n);
# - the number of such paths.
# A path is obtained by repeatedly moving in the grid one step north, south,
# west, or east.


import sys
from random import seed, randint


def display_grid():
    for row in grid:
        print(' '.join(f'{e:{len(str(upper_bound))}}' for e in row))


def find_path(new_position, new_value):
    a = new_position[0]
    b = new_position[1]
    up, down, left, right = 1, 1, 1, 1
    if a == 0 or grid[a - 1][b] != new_value + 1:
        up = 0
    if a == dim - 1 or grid[a + 1][b] != new_value + 1:
        down = 0
    if b == dim - 1 or grid[a][b + 1] != new_value + 1:
        right = 0
    if b == 0 or grid[a][b - 1] != new_value + 1:
        left = 0
    if (up or down or left or right) == 0:
        return new_value, 1
    else:
        value_list = [0, 0, 0, 0]
        nb_of_paths_list = [0, 0, 0, 0]
        if up:
            value_list[0], nb_of_paths_list[0] = find_path([a - 1, b], new_value + 1)
        if down:
            value_list[1], nb_of_paths_list[1] = find_path([a + 1, b], new_value + 1)
        if right:
            value_list[2], nb_of_paths_list[2] = find_path([a, b + 1], new_value + 1)
        if left:
            value_list[3], nb_of_paths_list[3] = find_path([a, b - 1], new_value + 1)
        value = max(value_list)
        nb_of_paths = 0
        for i in range(4):
            if value_list[i] == value:
                nb_of_paths += nb_of_paths_list[i]
        return value, nb_of_paths


def value_and_number_of_longest_paths():
    values = []
    nb_of_paths_of_values = []
    for i in range(dim):
        for j in range(dim):
            if grid[i][j] != 0:
                continue
            value, nb_of_paths = find_path([i, j], 0)
            values.append(value)
            nb_of_paths_of_values.append(nb_of_paths)
    max_value = max(values)
    nb_of_paths_of_max_value = 0
    for n in range(len(nb_of_paths_of_values)):
        if values[n] == max_value:
            nb_of_paths_of_max_value += nb_of_paths_of_values[n]
    return max_value, nb_of_paths_of_max_value
    # REPLACE THE RETURN STATEMENT WITH YOUR CODE


# POSSIBLY DEFINE OTHER FUNCTIONS

provided_input = input('Enter three integers: ').split()
if len(provided_input) != 3:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    for_seed, dim, upper_bound = (abs(int(e)) for e in provided_input)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randint(0, upper_bound) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

max_value, nb_of_paths_of_max_value = value_and_number_of_longest_paths()
if not nb_of_paths_of_max_value:
    print('There is no 0 in the grid.')
else:
    print('The longest paths made up of consecutive numbers starting '
          f'from 0 go up to {max_value}.'
          )
    if nb_of_paths_of_max_value == 1:
        print('There is one such path.')
    else:
        print('There are', nb_of_paths_of_max_value, 'such paths.')
