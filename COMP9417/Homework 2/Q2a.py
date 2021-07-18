import numpy as np

A = np.array([[1, 0, 1, -1], [-1, 1, 0, 2], [0, -1, -2, 1]])
X = np.array([[1], [1], [1], [1]])
AT = np.transpose(A)
b = np.array([[1], [2], [3]])
k = 0
D = np.dot(AT, np.dot(A, X) - b)
value_D = np.linalg.norm(D)
x_list = []
for i in X:
    x_list.append(i[0])
print(f'k = {k}, x = {x_list}')
while value_D >= 0.001:
    x_list = []
    X = X - 0.1 * D
    D = np.dot(AT, np.dot(A, X) - b)
    value_D = np.linalg.norm(D)
    k += 1
    for i in X:
        x_list.append(i[0])
    print(f'k = {k}, x = {x_list}')
