# importing the dependencies
import numpy as np # linear algebra
import pandas as pd # dataframe
import tensorflow as tf # Machine learning
from glob import glob # file handling
from tqdm import tqdm # progress bar
from collections import deque # for simpler implementation of memory

import matplotlib.pyplot as plt # visualisation


def format_price(price):
    return ("-$" if price < 0 else "$") + "{0:.2f}".format(abs(price))


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# function to get the state
def get_state(data, t, n):
    d = t - n + 1
    if d >= 0:
        block = data[d:t + 1]
    else:
        # pad with t0
        block = -d * [data[0]] + data[0:t + 1].tolist()

    # block = data[d:t + 1] if d >= 0 else -d * [data[0]] + data[0:t + 1] # pad with t0

    # get results
    res = []
    for i in range(n - 1):
        res.append(sigmoid(block[i + 1] - block[i]))

    # return numpy array
    return np.array([res])

# load the csv file
path_folder = './data_raw/'
file_path = glob(path_folder + '*.csv')[0]
stock_name = file_path.split('.')[-2].split('/')[-1]
data = pd.read_csv(file_path)

# constants
LOG = False
episode_count = 10
window_size = 100
data = data['Close'].values # what our data is
len_data = len(data) - 1 # total information length
batch_size = 32 # minibatch size

# logs
loss_global = []
profits_global = []

plt.figure(figsize = (20, 8))
plt.plot(data)
plt.title(stock_name + '- Amazon', fontsize = 18)
plt.show()