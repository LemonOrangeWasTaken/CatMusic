import os
import tensorflow as tf
import keras
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
mnist = tf.keras.datasets.mnist
(x, y), (tx, ty) = mnist.load_data()

type(x)
x.shape
type(y)
y.shape

sample = x[0].flatten()

sample.shape
sample = tf.reshape(sample,(1,784,1))
sample.shape

x.shape
bruhx = x[:300]
xx = x[300:600]
f_x = tf.reshape(bruhx,(300,1,784))
more_x = tf.reshape(xx,(300,1,784))

new_cost_function = lambda inp, oup : tf.math.multiply(tf.math.multiply(tf.losses.binary_crossentropy(inp, oup), np.e), tf.keras.losses.categorical_crossentropy(inp, oup))

a = [0.,1.,0.,0.,0.,0.,1.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,1.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]
# b = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
# b = [1.,1.,1.,1.,1.,1.,1.,1.]
# b = [0.5,1.,0.5,0.5,0.5,0.5,1.,0.5]
b = [0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001]
# b = [0.01,1.,0.001,0.01,0.01,0.001,1.,0.01]
# b = [[0.2,0.8,0.2,0.1,0.3,0.2,0.7,0.18],[0.2,0.3,0.75,0.1,0.3,0.2,0.45,0.18],[0.2,0.8,0.67,0.1,0.4,0.2,0.7,0.18]]
# b = [0.,1.,0.,0.,0.,0.,1.,0.]

a = np.array(a)
b = np.array(b)

def normalize(arr, t_min, t_max):
    norm_arr = []
    diff = t_max - t_min
    diff_arr = max(arr) - min(arr)
    for i in arr:
        temp = (((i - min(arr))*diff)/diff_arr) + t_min
        norm_arr.append(temp)
    return norm_arr

tf.nn.softmax_cross_entropy_with_logits(labels=a, logits=b).numpy()
tf.losses.binary_crossentropy(a, b).numpy()
tf.keras.losses.categorical_crossentropy(a, b).numpy()
new_cost_function(a, b).numpy()

def getCustomLoss(train_in, gen_in):
    match = 0
    unmatch = 0
    min_thre = 0.3
    max_thre = 0.9

np.average(tf.losses.mean_squared_error(a, b).numpy())

f_x.shape
more_x.shape

model = Sequential()

model.add(LSTM(784, batch_input_shape=((None, 1, 784)), activation='relu', return_sequences=True))
model.add(LSTM(100, return_sequences=True))
model.add(LSTM(2))
model.compile(loss='sparse_categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(lr=1e-3), metrics=['accuracy'])

sample_output = model(more_x)
sample_output.shape
