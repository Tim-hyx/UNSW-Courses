# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Randomly generates a grid with 0s and 1s, whose dimension is controlled
# by user input, as well as the density of 1s in the grid, and finds out,
# for given step_number >= 1 and step_size >= 2, the number of stairs of
# step_number many steps, with all steps of size step_size.
#
# A stair of 1 step of size 2 is of the form
# 1 1
#   1 1
#
# A stair of 2 steps of size 2 is of the form
# 1 1
#   1 1
#     1 1
#
# A stair of 1 step of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#
# A stair of 2 steps of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#         1
#         1 1 1
#
# The output lists the number of stairs from smallest step sizes to largest
# step sizes, and for a given step size, from stairs with the smallest number
# of steps to stairs with the largest number of stairs.


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0))
                              for j in range(len(grid))
                              )
              )


try:
    arg_for_seed, density, dim = (int(x) for x in
                                  input('Enter three positive integers: ').split()
                                  )
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

# INSERT YOUR CODE HERE
grid_dict, stairs, size = defaultdict(dict), defaultdict(list), 2
# max of size of stair, depending on even or odd
if dim % 2:
    max_size = (dim + 1) / 2
else:
    max_size = dim / 2
while size <= int(max_size):
    used, i = set(), 0
    while i <= len(grid) - 1:
        j = 0
        while j <= len(grid) - 1:
            check = 0
            if (i, j) not in used and (i <= len(grid) - 1) and (
                    j + size - 1 <= len(grid) - 1):  # check the boundary
                n = 0
                # check whether there's 0 in range j to j+n
                while n <= size - 1:
                    if grid[i][j + n] == 0:
                        break
                    else:
                        check += 1
                    n += 1
                if check == size:
                    x, y, steps = i, j + size - 1, 0
                    while (x + size - 1 <= len(grid) - 1) and (y + size - 1 <= len(grid) - 1):  # check the boundary
                        check_x, check_y, p, q = 0, 0, 1, 0
                        # check whether there's 0 in the middle vertical line
                        while p <= size - 2:
                            if grid[x + p][y] == 0:
                                break
                            else:
                                check_x += 1
                            p += 1
                        # check whether there's 0 in the next level line
                        while q <= size - 1:
                            if grid[x + size - 1][y + q] == 0:
                                break
                            else:
                                check_y += 1
                            q += 1
                        if check_x != size - 2:
                            break
                        if check_y != size:
                            break
                        else:
                            used.add((x + (size - 1), y))  # add the next level start to used in order to extended
                            steps += 1
                        y += (size - 1)
                        x += (size - 1)
                    if steps > 0:
                        if steps in grid_dict[size].keys():
                            grid_dict[size][steps] += 1
                        else:
                            grid_dict[size][steps] = 1
            j += 1
        i += 1
    size += 1
for num_size in grid_dict:
    stairs[num_size] = [(num_step, grid_dict[num_size][num_step]) for num_step in grid_dict[
        num_size]]  # A dictionary whose keys are step sizes, and whose values are pairs of the form
for num in stairs:
    stairs[num] = sorted(stairs[num], key=lambda x: x[
        0])  # (number_of_steps, number_of_stairs_with_that_number_of_steps_of_that_step_size)
for j in sorted(stairs):
    print()
    print(f'For steps of size {j}, we have:')
    for nb_step, nb_stair in stairs[j]:
        if nb_stair > 1:
            stair = 'stairs'
        else:
            stair = 'stair'
        if nb_step > 1:
            step = 'steps'
        else:
            step = 'step'
        print(f'     {nb_stair} {stair} with {nb_step} {step}')
