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
i = 0
error = 0
while i < len(predicted_boards):
    #print(predicted_boards[random.randint(0,100)])
    try:
        vector2string(predicted_boards[i])
    except:
        error = error + 1
        if error % 100 == 0:
            print(str(error))
            print('---')
            print(str(i))
        #print('Al ' + str(error) + ' kromme borden van de ' + str(i) ' gecheckte borden gevonden')
        

print('Aantal kromme borden: ' + str(error) + ' van totaal ' + str(len(predicted_boards)) + ' borden')




