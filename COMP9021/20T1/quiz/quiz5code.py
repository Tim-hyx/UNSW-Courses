# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# In both functions below, grid is supposed to be a sequence of strings
# all of the same length, consisting of nothing but spaces and *s,
# and represent one or more "full polygons" that do not "touch" each other.

def display(*grid):
    for i in grid:
        print(' '.join(i))
    # REPLACE pass ABOVE WITH YOUR CODE


def boundary(grid, y, x):
    location = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    count = 0
    len_y = len(grid)
    len_x = len(grid[0])
    for y_location, x_location in location:
        new_y = y + y_location
        new_x = x + x_location
        if 0 <= new_x < len_x and 0 <= new_y < len_y and grid[new_y][new_x] != ' ':
            count += 1
    if count < 4:
        return True
    else:
        return False


def loop(grid, y, x):
    location = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    grid[y][x] = '1'
    len_y = len(grid)
    len_x = len(grid[0])
    for y_location, x_location in location:
        new_y = y + y_location
        new_x = x + x_location
        if 0 <= new_x < len_x and 0 <= new_y < len_y and grid[new_y][new_x] == '*' and boundary(grid, new_y, new_x):
            loop(grid, new_y, new_x)


def display_leftmost_topmost_boundary(*grid):
    left_y = 0
    left_x = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '*':
                left_y = y
                left_x = x
                break
        if left_y and left_x:
            break
    list_grid = []
    for i in grid:
        a = list(i)
        list_grid.append(a)
    loop(list_grid, left_y, left_x)
    for j in list_grid:
        b = ''.join(j)
        b = b.replace('*', ' ')
        b = b.replace('1', '*')
        print(' '.join(b))

# REPLACE pass ABOVE WITH YOUR CODE

# POSSIBLY DEFINE OTHER FUNCTIONS
