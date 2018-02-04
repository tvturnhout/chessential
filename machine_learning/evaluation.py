import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
import sys
sys.path.insert(0, './../functions')
from file_reader import readdata
import numpy as np
from run_chessential import predict


X, y = readdata('./../data/20180204T0021boards.h5')

print(predict(X))
