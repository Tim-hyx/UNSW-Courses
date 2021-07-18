import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 0, 1, -1], [-1, 1, 0, 2], [0, -1, -2, 1]])
X = np.array([[1], [1], [1], [1]])
AT = np.transpose(A)
b = np.array([[1], [2], [3]])
k = 0
a = 0.1
D = np.dot(AT, np.dot(A, X) - b)
value_D = np.linalg.norm(D)
alpha_list = [0.1]
x_list = []
for i in X:
    x_list.append(i[0])
k = 0
print(f'k = {k}, x = {x_list},α = 0.1')
while value_D >= 0.001:
    k += 1
    x_list = []
    X = X - a * D
    for i in X:
        x_list.append(i[0])
    D = np.dot(AT, np.dot(A, X) - b)
    value_D = np.linalg.norm(D)
    a = (np.dot(np.dot(np.transpose(np.dot(A, X)), A), D) - np.dot(np.dot(np.transpose(b), A), D)) / (
        np.dot(np.dot(np.transpose(np.dot(A, D)), A), D))
    alpha_list.append(a[0][0])
    print(f'k = {k}, x = {x_list},α = {a[0][0]}')
plt.plot(alpha_list)
plt.show()
