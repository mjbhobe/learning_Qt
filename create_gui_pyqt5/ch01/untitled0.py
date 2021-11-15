# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 23:45:48 2021

@author: manis
"""
import random
import numpy as np
import pandas as pd
from pylab import mpl, plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'SF UI Text'

x, y = make_blobs(n_samples=500, centers=4, random_state=SEED,
                  cluster_std=2.50)
print(x.shape, y.shape)
plt.figure(figsize=(6,4))
plt.scatter(x[:,0], x[:,1], c='steelblue')

# run the classification
model = KMeans(n_clusters=4, random_state=SEED)
model.fit(x, y)

# predict
y_ = model.predict(x)
plt.scatter(x[:,0], x[:,1], c=y_, cmap='coolwarm')



def f(x):
    return 2 * x ** 2 - x ** 3 / 3

x = np.linspace(-2, 4, 25)
y = f(x)
plt.figure(figsize=(10,6))
plt.plot(x, y, 'o')

# for simple linear regression using OLS
# y = m * x + c
# c = cov(x, y)/var(x)
# m = mean(y) - c * mean(x)

c = np.cov(x, y, ddof=0)[0,1] / np.var(x)
m = np.mean(y) - c * np.mean(x)
print(f"m = {m:.4f} and c = {c:.4f}")
y_ = m * x + c
plt.figure(figsize=(10,6))
plt.plot(x, y, 'o', label='data')
plt.plot(x, y_, c='firebrick', label='prediction')
plt.legend(loc='best')

plt.plot(x, y, 'ro', label='sample data')
for deg in [1, 2, 3]:
    reg = np.polyfit(x, y, deg=deg)
    y_ = np.polyval(reg, x)
    MSE = ((y - y_) ** 2).mean()
    #print(f'deg={deg} | MSE={MSE:.5f}')
    plt.plot(x, y_, label=f'deg={deg}|MSE={MSE:.3f}')
plt.legend(loc='best')
plt.show()

# let's try fitting a neural network
from sklearn.neural_network import MLPRegressor

model = MLPRegressor(hidden_layer_sizes=3*[256],
                     learning_rate_init=0.03,
                     max_iter=5000)
model.fit(x.reshape(-1,1), y)
y_ = model.predict(x.reshape(-1, 1))
MSE = ((y - y_) ** 2).mean()

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'ro', label='sample data')
plt.plot(x, y_, lw=3.0, label='dnn estimation')
plt.legend();

import tensorflow as tf

tf.random.set_seed(SEED)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(256, activation='relu', input_dim=1),
    tf.keras.layers.Dense(1, activation='linear')
])
model.compile(loss='mse', optimizer='rmsprop', metrics=['mae'])

plt.figure(figsize=(10,6))
plt.plot(x, y, 'ro', label='sample data')
for r in range(1,6):
    model.fit(x, y, epochs=100, verbose=0)
    y_ = model.predict(x)
    MSE = ((y - y_.flatten()) ** 2).mean()
    print(f"round {r} - MSE : {MSE:.4f}")
    plt.plot(x, y_, '--', label=f'round={r}|MSE={MSE:.3f}')
plt.legend(loc='best')
plt.show()

# classification using Keras
n, f = 100, 5
np.random.seed(100)

x = np.random.randint(0, 2, (n , f))
y = np.random.randint(0, 2, (n,))

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(256, activation='relu', input_dim=f),
    # tf.keras.layers.Dense(128, activation='relu'),
    # tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(loss='binary_crossentropy', optimizer='rmsprop', 
              metrics=['acc'])
hist = model.fit(x, y, epochs=50, verbose=0)
y_ = np.where(model.predict(x).flatten() > 0.5, 1, 0)
y, y_
res = pd.DataFrame(hist.history)
res.plot(figsize=(10,6))
