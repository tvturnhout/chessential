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
from vectorizer import vector2board, vector2string, board2vector
from IPython.display import SVG
import chess
from telebot import TeleBot

app = TeleBot(__name__)


X, y = readdata('./../data/20180204T0021boards.h5')

predicted_boards = predict(X)


legal_counter = 0
for item in predicted_boards:
    bord, illegal = vector2string(item)
    if illegal:
        legal_counter = legal_counter + 1

    print(str(legal_counter) + '/' + str(len(predicted_boards)))
print(str((1-float(legal_counter)/float(len(predicted_boards)))*100) + '%')


#very hacky not ready for production yet
logic_counter = 0
i = 0
for item in X:

    board = vector2board(item)
    legal_moves = board.legal_moves
    potential_moves = []
    for item2 in legal_moves:
        potential_moves.append(item2)

    logical_boards = []
    for move in potential_moves:
        board = vector2board(item)
        board.push(move)
        logical_boards.append(board2vector(board))


    temp_list1 = y.tolist()
    temp_list2 = []
    for listitem in temp_list1[i]:
        temp_list2.append(int(listitem))
   

    for board_check in logical_boards:
        temp_list3 = []
        for listitem in board_check.tolist():
            temp_list3.append(int(listitem))
        if temp_list2 == temp_list3:
            logic_counter = logic_counter + 1
 
    i = i + 1
    print(str(i) + '/' + str(len(X)))

    print(str(float(logic_counter)/float(len(predicted_boards))*100) + '%')  



