import chess
import time
import numpy as np

PossibleEntries = '.prnbqkPRNBQK'

def board2vector(Board):
    board_asString0 = str(Board)
    board_asString = board_asString0.replace(" ", "")
    board_asString = board_asString.replace('\n', "")
    board_asvector = np.zeros(13*64)
    for b in range(len(board_asString)):
        piece = board_asString[b]
        for it in range(len(PossibleEntries)):
            board_asvector[b*13+it] = int(piece is PossibleEntries[it])
    return board_asvector

def vector2string(Vector):
    board_asString2 = ''
    for it in range(0,len(Vector),len(PossibleEntries)):
        board_asString2 += PossibleEntries[int(np.where(Vector[it:it + 13])[0])]
    board_asString = board_asString2[0]
    for it in range(1,len(board_asString2)):
        if it % 8>0:
            board_asString +=  ' ' + board_asString2[it]
        else:
            board_asString +=  '\n' + board_asString2[it]
    return board_asString

if __name__ is '__main__':
    Board = chess.Board()
    start = time.time()
    number = 10000
    for i in range(number):
        Vector = board2vector(Board)
    end = time.time()
    print('Took me {} ms per board'.format((end-start)/number*1e3))

    start = time.time()
    for i in range(number):
        String = vector2string(Vector)
    end = time.time()
    print('Took me {} ms per board'.format((end-start)/number*1e3))



