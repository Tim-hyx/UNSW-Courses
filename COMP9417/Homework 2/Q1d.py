import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np

# The data.csv is located in the desktop, so I hardcode the file name
df = pd.read_csv('C:/Users/TimHuang/Desktop/Q1.csv')
df = df[:500]
df1 = df.copy()
np.random.seed(12)
coef_list = []
for i in range(10000):
    random_list = np.random.randint(0, 500, size=500)
    df3 = df1.reindex(index=random_list)
    train_x = df3.drop(['Y'], axis=1)
    train_y = df3['Y']
    cls = LogisticRegression(C=1, solver='liblinear', penalty="l1")
    cls.fit(train_x, train_y)
    coef = cls.coef_
    coef_list.append(coef[0])
df2 = pd.DataFrame(data=coef_list)
bottom_list, height_list, color_list, num_list, mean_list = [], [], [], [], []
for i in range(45):
    num_list.append(i)
    mean_list.append(df2[i].mean())
    res = df2.sort_values(by=i)
    bottom_list.append(res.iloc[499, i])
    height_list.append(res.iloc[9499, i] - res.iloc[499, i])
    if res.iloc[499, i] <= 0 <= res.iloc[9499, i]:
        color_list.append('red')
    else:
        color_list.append('blue')
plt.scatter(x=num_list, y=mean_list, zorder=10)
plt.bar(x=num_list, height=height_list, bottom=bottom_list, color=color_list, zorder=5)
plt.show()
