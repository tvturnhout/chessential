import chess
import random
from vectorizer import *
import numpy as np
import h5py


boards = []
while len(boards) < 1000:
    board = chess.Board()

    i = 0
    while not i > 50 or board.is_game_over() or board.is_insufficient_material() or board.is_stalemate() or board.is_seventyfive_moves():

        legal_moves = board.legal_moves
        potential_moves = []
        for item in legal_moves:
            potential_moves.append(item)

        i = i + 1 
        move = random.choice(potential_moves)
        board.push(move)
        #use the transformation function before adding it to board
        boards.append(Board2Vector(board))
        #print(Board2Vector(board))
        #print(move)
        #print(board)
        #print(len(boards))
        
        if len(boards) % 100 == 0:
            print("Added " + str(len(boards)) + " boards to database")

h5f = h5py.File('boards.h5', 'w')
h5f.create_dataset('input_boards', data=boards)


'''
np.savetxt('test.txt', boards , delimiter=",", newline="\n", fmt ="%d") 

outF = open("myOutFile.txt", "w")
for line in boards:
outF.write(str(line))
outF.write("\n")
outF.close()
'''



