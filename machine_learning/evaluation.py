import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
import sys
sys.path.insert(0, './../functions')
from file_reader import readdata
import numpy as np
from run_chessential import predict
import random
from vectorizer import vector2board, vector2string
from IPython.display import SVG
import chess

X, y = readdata('./../data/20180204T0021boards.h5')

predicted_boards = predict(X)

print(predicted_boards[5])
print(predicted_boards[15])
print(vector2string(predicted_boards[5]))

print(vector2string(predicted_boards[10]))





