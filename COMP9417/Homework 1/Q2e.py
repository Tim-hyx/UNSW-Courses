import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
import math

# The data.csv is located in the desktop, so I hardcode the file name
df = pd.read_csv('C:/Users/TimHuang/Desktop/data.csv')
df2 = df['Y']
df.drop(df.columns[len(df.columns) - 1], axis=1, inplace=True)
mean_list = []
square_mean_list = []
df1 = df.copy()
for col in df.columns:
    mean = round(df[col].mean(), 2)
    mean_list.append(mean)
    df1[col] = df1[col] - mean
    df[col] = (df[col] - mean) ** 2
    square_mean = round(df[col].mean() ** 0.5, 2)
    square_mean_list.append(square_mean)
    df1[col] /= square_mean

num_list = [0.01, 0.1, 0.5, 1, 1.5, 2, 5, 10, 20, 30, 50, 100, 200, 300]
res_list = []
for i in range(len(num_list)):
    reg = Lasso(alpha=num_list[i])
    reg.fit(df1, df2)
    res = reg.coef_
    res_list.append(res)
    num_list[i] = math.log(num_list[i])
df3 = pd.DataFrame(res_list)
label_list = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8']
color_list = ['red', 'brown', 'green', 'blue', 'orange', 'pink', 'purple', 'grey']
for i in range(len(label_list)):
    plt.plot(num_list, df3[i], color_list[i], label=label_list[i])
plt.xlabel('log(λ)')
plt.ylabel('the value of the coefficient')
plt.legend()
plt.show()
