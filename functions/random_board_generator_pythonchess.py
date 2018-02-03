import chess
import random
from vectorizer import Board2Vector
from call_engine import best_board
import numpy as np
import h5py
import datetime

boards = []
Nextboards = []

fname = 'Data/' + datetime.datetime.now().strftime('%Y%m%dT%H%M') + 'boards.h5'
h5f = h5py.File(fname, 'w')
dsI = h5f.create_dataset("input_boards", (832,0), maxshape=(832,None), dtype='f', chunks=(832,1000))
dsO = h5f.create_dataset("output_boards", (832,0), maxshape=(832,None), dtype='f', chunks=(832,1000))
h5f.close()

N = 0
while N < 1000:
    board = chess.Board()

    i = 0
    while not i > 50 \
            and not board.is_game_over() \
            and not board.is_insufficient_material() \
            and not board.is_stalemate() \
            and not board.is_seventyfive_moves():
        legal_moves = board.legal_moves
        potential_moves = []
        for item in legal_moves:
            potential_moves.append(item)

        i = i + 1
        move = random.choice(potential_moves)
        board.push(move)
        #use the transformation function before adding it to board
        boards.append(Board2Vector(board))

        Nextboards.append(Board2Vector(best_board(board,100)))
        #print(Board2Vector(board))
        #print(move)
#        if board.is_game_over():
#            print('is_game_over')
#            print(board)
#        if board.is_stalemate():
#            print('is_stalemate')
#            print(board)
#        if board.is_seventyfive_moves():
#            print('is_seventyfive_moves')
#            print(board)
#        if board.is_insufficient_material():
#            print('is_insufficient_material')
#            print(board)
        #print(len(boards))

    h5f = h5py.File(fname, 'a')

    dsetIn = h5f["input_boards"]
    dsetOut = h5f["output_boards"]

    curlength = dsetIn.shape[1]
    dsetIn.resize(curlength+len(boards), axis=1)
    dsetIn[:,curlength:]=np.transpose(np.array(boards))

    curlength = dsetOut.shape[1]
    dsetOut.resize(curlength+len(Nextboards), axis=1)
    dsetOut[:,curlength:]=np.transpose(np.array(Nextboards))

    N = dsetIn.shape[1]
    h5f.close()

    boards = []
    Nextboards = []
    print("Added " + str(N) + " boards to database")
#h5f = h5py.File('boards.h5', 'w')
#h5f.create_dataset('input_boards', data=boards)
#h5f.create_dataset('output_boards', data=Nextboards)
h5f.close()

'''
np.savetxt('test.txt', boards , delimiter=",", newline="\n", fmt ="%d")

outF = open("myOutFile.txt", "w")
for line in boards:
outF.write(str(line))
outF.write("\n")
outF.close()
'''



