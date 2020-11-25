# Written by Eric Martin for COMP9021


from itertools import count


def is_magic_square(square):
    n = len(square)
    if any(len(line) != n for line in square):
        return False
    if {number for line in square for number in line} !=\
                                               set(range(1, n ** 2 + 1)):
        return False
    the_sum = n * (n ** 2 + 1) // 2
    if not_good_lines(square, the_sum):
        return False
    if not_good_lines([[square[i][j] for i in range(n)] for j in range(n)],
                      the_sum
                    ):
        return False
    if sum(square[i][i] for i in range(n)) != the_sum:
        return False
    if sum(square[i][n - 1 - i] for i in range(n)) != the_sum:
        return False
    return True

def not_good_lines(square, the_sum):
    return any(sum(line) != the_sum for line in square)

def print_square(square):
    field_width = len(str(len(square) ** 2))
    for line in square:
        print(' '.join(f'{number:{field_width}}' for number in line))

def bachet_magic_square(n):
    if n % 2 == 0:
        return
    N = 2 * n - 1
    square = [[None] * N for _ in range(N)]
    k = count(1)
    for i in range(n):
        for j in range(n):
            square[i + j][j + n - i - 1] = next(k)
    s = (n - 1) // 2
    for _ in range(4):
        for i in range(s):
            for j in range(n - i - 1, n + i, 2):
                square[i + n][j] = square[i][j]
        square = [[square[N - 1 - i][j] for i in range(N)] for j in range(N)]
    return [line[s : s + n] for line in square[s : s + n]]

def siamese_magic_square(n):
    if n % 2 == 0:
        return
    square = [[None] * n for _ in range(n)]
    k = count(1)
    i, j = 0, n // 2
    square[i][j] = next(k)
    for _ in range(n ** 2 - 1):
        i1, j1 = (i - 1) % n, (j + 1) % n
        i, j = (i + 1, j) if square[i1][j1] else (i1, j1)
        square[i][j] = next(k)
    return square

def lux_magic_square(n):
    if n < 6 or n % 4 != 2:
        return
    k = count(1)
    square = [[None] * n for _ in range(n)]
    def process_U_cell():
        square[2 * i][2 * j] = next(k)
        square[2 * i + 1][2 * j] = next(k)
        square[2 * i + 1][2 * j + 1] = next(k)
        square[2 * i][2 * j + 1] = next(k)
    def process_L_cell():
        square[2 * i][2 * j + 1] = next(k)
        square[2 * i + 1][2 * j] = next(k)
        square[2 * i + 1][2 * j + 1] = next(k)
        square[2 * i][2 * j] = next(k)
    def process_X_cell():
        square[2 * i][2 * j] = next(k)
        square[2 * i + 1][2 * j + 1] = next(k)
        square[2 * i + 1][2 * j] = next(k)
        square[2 * i][2 * j + 1] = next(k)
    N = n // 2
    patterns = {(i, j): process_L_cell for i in range(N // 2 + 1)
                                           for j in range(N)
               }
    patterns.update(((N // 2 + 1, j), process_U_cell) for j in range(N))
    patterns.update(((i, j), process_X_cell) for i in range(N // 2 + 2, N)
                                                 for j in range(N)
                   )
    patterns[N // 2, N // 2], patterns[N // 2 + 1, N // 2] =\
                                               patterns[N // 2 + 1, N // 2],\
                                               patterns[N // 2, N // 2]
    i, j = 0, N // 2
    patterns[i, j]()
    for _ in range(N ** 2 - 1):
        i1, j1 = (i - 1) % N, (j + 1) % N
        i, j = (i + 1, j) if square[2 * i1][2 * j1] else (i1, j1)
        patterns[i, j]()
    return square
