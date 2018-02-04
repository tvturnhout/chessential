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

def vector2board(Vector):
    board_asString2 = ''
    for it in range(0,len(Vector),len(PossibleEntries)):
        board_asString2 += PossibleEntries[int(np.where(Vector[it:it + 13])[0])]

    board_asString3 = ''
    e=0
    r=0
    for it in range(len(board_asString2)):
        r += 1
        char = board_asString2[it]
        if char in PossibleEntries[1:]:
            if e>0:
                board_asString3 += str(e)
                e=0
            board_asString3 += char
        elif char is PossibleEntries[0]:
            e += 1
        if r is 8:
            if e>0:
                board_asString3 += str(e)
                e=0
            board_asString3 += '/'
            r = 0
    board_asString3 = board_asString3[:-1] + ' w - - 2 1'

#
#    board_asString = board_asString2[0]
#    for it in range(1,len(board_asString2)):
#        if it % 8>0:
#            board_asString +=  ' ' + board_asString2[it]
#        else:
#            board_asString +=  '\n' + board_asString2[it]
    return chess.Board(board_asString3)

def vector2string(Vector):
    board_asString2 = ''
    for it in range(0,len(Vector),len(PossibleEntries)):
        pieces = np.where(Vector[it:it + 13])[0]
        if len(pieces) >1:
            board_asString2 += 'X'
        else:
            board_asString2 += PossibleEntries[int(pieces[0])]
    board_asString3 = ''
    r = 0
    for p in board_asString2:
        r += 1
        board_asString3 += p
        if r is 8:
            board_asString3 += '\n'
            r=0

#
#    board_asString = board_asString2[0]
#    for it in range(1,len(board_asString2)):
#        if it % 8>0:
#            board_asString +=  ' ' + board_asString2[it]
#        else:
#            board_asString +=  '\n' + board_asString2[it]
    return board_asString3

if __name__ is '__main__':
    Board = chess.Board()
    start = time.time()
    number = 1
    for i in range(number):
        Vector = board2vector(Board)
    end = time.time()
    print('Took me {} ms per board'.format((end-start)/number*1e3))

    start = time.time()
    for i in range(number):
        Board = vector2board(Vector)
    end = time.time()
    print(vector2string(Vector))
    print('Took me {} ms per board'.format((end-start)/number*1e3))



