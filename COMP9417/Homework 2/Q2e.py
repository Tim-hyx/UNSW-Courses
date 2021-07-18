import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import jax.numpy as jnp
from jax import grad
import matplotlib.pyplot as plt

df = pd.read_csv('Q2.csv')
df = df.dropna()
df_price = df['price']
df_price = df_price.reset_index()
df_price = df_price.drop('index', 1)
df = pd.DataFrame(df, columns=['age', 'nearestMRT', 'nConvenience'])
df_x = MinMaxScaler()
x = df_x.fit_transform(df)
train_x = x[:int(len(x) / 2)]
train_x = np.insert(train_x, 0, values=1, axis=1)
test_x = x[int(len(x) / 2):]
test_x = np.insert(test_x, 0, values=1, axis=1)
train_y = df_price[:int(len(x) / 2)]
test_y = df_price[int(len(x) / 2):]
train_x = jnp.array(train_x)
train_y = jnp.array(train_y)
test_x = jnp.array(test_x)
test_y = jnp.array(test_y)


def loss(W):
    preds = jnp.dot(train_x, W)
    label_probs = jnp.sqrt(((train_y - preds) ** 2) * 0.25 + 1) - 1
    return jnp.mean(label_probs)


def loss_test(W):
    preds = jnp.dot(test_x, W)
    label_probs = jnp.sqrt(((test_y - preds) ** 2) * 0.25 + 1) - 1
    return jnp.mean(label_probs)


loss_list = []
W = jnp.array([[1.0], [1.0], [1.0], [1.0]])
W_grad = grad(loss)(W)
loss_ = loss(W)
loss_list.append(loss_)
W = W - W_grad
W_grad = grad(loss)(W)
new_loss = loss(W)
loss_list.append(new_loss)
i = 0
while loss_ - new_loss >= 0.0001:
    W = W - W_grad
    W_grad = grad(loss)(W)
    loss_ = new_loss
    new_loss = loss(W)
    loss_list.append(new_loss)
    i += 1
plt.plot(loss_list)
plt.show()
print(f'The number of iterations is {i}')
print(f'The final weight is {W}')
print(f'The train loss is {new_loss}')

W = jnp.array([[1.0], [1.0], [1.0], [1.0]])
W_grad = grad(loss_test)(W)
loss_ = loss_test(W)
W = W - W_grad
W_grad = grad(loss_test)(W)
new_loss = loss_test(W)
while loss_ - new_loss >= 0.0001:
    W = W - W_grad
    W_grad = grad(loss_test)(W)
    loss_ = new_loss
    new_loss = loss_test(W)
print(f'The test loss is {new_loss}')
