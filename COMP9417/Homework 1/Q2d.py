import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge,LinearRegression

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

sample = []
a = 0
res_list = []
while a <= 50.1:
    sample.append(round(a, 1))
    a += 0.1
for i in sample:
    E = 0
    for j in range(0, 38):
        reg = Ridge(alpha=i)
        test_x = df1[j:j + 1]
        train_x = df1.drop([j])
        train_y = df2.drop([j])
        reg.fit(train_x, train_y)
        pred_y = reg.predict(test_x)
        test_y = df2[j]
        e = (pred_y - test_y) ** 2
        E += e
    value = E / 38
    res_list.append(value)
plt.plot(sample, res_list)
plt.show()
print(min(res_list))

E = 0
ols_list = []
for j in range(0, 38):
    reg = LinearRegression()
    test_x = df1[j:j + 1]
    train_x = df1.drop([j])
    train_y = df2.drop([j])
    reg.fit(train_x, train_y)
    pred_y = reg.predict(test_x)
    test_y = df2[j]
    e = (pred_y - test_y) ** 2
    E += e
value = E / 38
ols_list.append(value)
print(min(ols_list))