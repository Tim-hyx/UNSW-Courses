from numpy import *

matrix = []
row = [float(_) for _ in input('input row1  : ').replace(',', ' ').split()]
matrix.append(row)
for i in range(2, len(row) + 1):
    row = [float(_) for _ in input(f'input row{i}  : ').replace(',', ' ').split()]
    matrix.append(row)
matrix = mat(matrix)
while True:
    command = input('input vector: ').replace(',', ' ').split()
    vector = mat([float(_) for _ in command])
    result = vector * matrix
    a, b, c = vector.tolist(), result.tolist(), []
    for i in range(len(a[0])):
        if a[0][i] * b[0][i] < 0:
            c.append(i)
    stable = (not len(c))
    print(f'{a[0]}\n{b[0]}\nstable: {stable}, unstable item: {c}')
