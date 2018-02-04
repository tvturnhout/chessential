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


counter = 0
for item in predicted_boards:
    bord, illegal = vector2string(item)
    if illegal:
        counter = counter + 1

    print(str(counter) + '/' + str(len(predicted_boards)))
print(str(float(counter)/float(len(predicted_boards))*100) + '%')






