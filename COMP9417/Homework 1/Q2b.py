import pandas as pd

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
for col in df1.columns:
    df1[col] = df1[col] ** 2
    print(df1[col].sum())