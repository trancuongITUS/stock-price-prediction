from sklearn.preprocessing import MinMaxScaler
from keras.layers import LSTM, Dropout, Dense
from keras.models import Sequential
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 20, 10

df = pd.read_csv('NSE-Tata-Global-Beverages-Limited.csv')
df.head()
