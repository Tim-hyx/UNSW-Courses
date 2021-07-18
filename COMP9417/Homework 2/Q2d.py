import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('C:/Users/TimHuang/Desktop/Q2.csv')
df = df.dropna()
df_price = df['price']
df_price = df_price.reset_index()
df_price = df_price.drop('index', 1)
df = pd.DataFrame(df, columns=['age', 'nearestMRT', 'nConvenience'])
df_x = MinMaxScaler()
x = df_x.fit_transform(df)
train_x = x[:int(len(x) / 2)]
test_x = x[int(len(x) / 2):]
train_y = df_price[:int(len(x) / 2)]
test_y = df_price[int(len(x) / 2):]
print(f'first row X_train: {train_x[0]}')
print(f'last row X_train: {train_x[-1]}')
print(f'first row X_test: {test_x[0]}')
print(f'last row X_test: {test_x[-1]}')
print(f"first row Y_train: {train_y.iloc[0]['price']}")
print(f"last row Y_train: {train_y.iloc[-1]['price']}")
print(f"first row Y_test: {test_y.iloc[0]['price']}")
print(f"last row Y_test: {test_y.iloc[-1]['price']}")
