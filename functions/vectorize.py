import chess
import time
import numpy as np
from call_engine import best_board

PossibleEntries = '.prnbqkPRNBQK'
PossibleEntriesFen =  'prnbqkPRNBQK'
EnPassantList = ['a3','b3','c3','d3','e3','f3','g3','h3','a6','b6','c6','d6','e6','f6','g6','h6',]

def board2vector(Board, legacy = False):
    if legacy:
        board_asString0 = str(Board)
        board_asString = board_asString0.replace(" ", "")
        board_asString = board_asString.replace('\n', "")
        board_asvector = np.zeros(13*64)
        for b in range(len(board_asString)):
            piece = board_asString[b]
            for it in range(len(PossibleEntries)):
                board_asvector[b*13+it] = int(piece is PossibleEntries[it])
    else:
        BoardAsFen = Board.fen()
        Content = BoardAsFen.split(' ')
        board_asvector = np.zeros(12*64+2+4+16+1+1)
        i = 0
        for piece in Content[0]:
            if piece in PossibleEntriesFen:
                for it in range(len(PossibleEntriesFen)):
                    board_asvector[i*12 + it] = int(piece is PossibleEntriesFen[it])
                i += 1
            elif piece is '/':
                board_asvector
            elif piece.isnumeric():
                emptyplaces = int(piece)
                for ite in range(emptyplaces):
                    for it in range(len(PossibleEntriesFen)):
                        board_asvector[i*12 + it] = int(0)
                    i += 1
        board_asvector[12*64] = int(Content[1] is 'w')
        board_asvector[12*64+1] = int(Content[1] is 'b')

        board_asvector[12*64+2] = int('K' in Content[2])
        board_asvector[12*64+3] = int('Q' in Content[2])
        board_asvector[12*64+4] = int('k' in Content[2])
        board_asvector[12*64+5] = int('q' in Content[2])

        for it in range(len(EnPassantList)):
            board_asvector[12*64+6+it] = int(Content[3] is EnPassantList[it])

        board_asvector[12*64+22] = int(Content[4])
        board_asvector[12*64+23] = int(Content[5])
    return board_asvector

def vector2board(Vector, legacy = False):
    if legacy:
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
        board_asString = board_asString3[:-1] + ' w - - 2 1'
    else:
        board_asString2 = ''
        Illegal = False
        e = 0
        r=0
        for it in range(0,len(PossibleEntriesFen)*64,len(PossibleEntriesFen)):
            r += 1
            pieces = np.where(Vector[it:it + len(PossibleEntriesFen)])[0]
            if len(pieces) > 1:
                board_asString2 += 'X'
                Illegal = True
            elif len(pieces) is 0:
                e += 1
            else:
                if e>0:
                    board_asString2 += str(e)
                    e=0
                board_asString2 += PossibleEntriesFen[int(pieces[0])]
            if r % 8 == 0:
                if e>0:
                    board_asString2 += str(e)
                    e=0
                if r<64:
                    board_asString2 += '/'

    #    12*64+2+4+16+1+1
        Color = np.where(Vector[12*64:12*64+2])[0]
        if len(Color) != 1:
            color2move = 'X'
            Illegal = True
        else:
            color2move = 'wb'[int(Color[0])]

        castlingrights = ''
        if Vector[12*64+2]:
            castlingrights += 'K'
        if Vector[12*64+3]:
            castlingrights += 'Q'
        if Vector[12*64+4]:
            castlingrights += 'k'
        if Vector[12*64+5]:
            castlingrights += 'q'
        if len(castlingrights) is 0:
            castlingrights = '-'

        EnPassant = np.where(Vector[12*64+6:12*64+6+16])[0]
        if len(EnPassant) > 1:
            enpassant = 'X'
            Illegal = True
        elif len(EnPassant) is 0:
            enpassant = '-'
        else:
            for it in range(len(EnPassantList)):
                if Vector[12*64+6+it]:
                    enpassant = EnPassantList[it]

        halfmoveclock = int(Vector[12*64+6+16])
        fullmovenumber = int(Vector[12*64+6+16+1])

        board_asString = board_asString2 + ' ' + color2move + ' ' + castlingrights + ' ' + enpassant + ' ' + str(halfmoveclock) + ' ' + str(fullmovenumber)
    return chess.Board(board_asString)
    #hallo

def vector2string(Vector, legacy = False):
    if legacy:
        board_asString2 = ''
        Illegal = False
        for it in range(0,len(Vector),len(PossibleEntries)):
            pieces = np.where(Vector[it:it + 13])[0]
            if len(pieces) != 1:
                board_asString2 += 'X'
                Illegal = True
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
    else:
        board_asString2 = ''
        Illegal = False
        for it in range(0,len(PossibleEntriesFen)*64,len(PossibleEntriesFen)):
            pieces = np.where(Vector[it:it + len(PossibleEntriesFen)])[0]
            if len(pieces) > 1:
                board_asString2 += 'X'
                Illegal = True
            elif len(pieces) is 0:
                board_asString2 += '.'
            else:
                board_asString2 += PossibleEntriesFen[int(pieces[0])]
        board_asString3 = ''
        r = 0
        for p in board_asString2:
            r += 1
            board_asString3 += p
            if r is 8:
                board_asString3 += '\n'
                r=0

    #    12*64+2+4+16+1+1
        Color = np.where(Vector[12*64:12*64+2])[0]
        if len(Color) != 1:
            color2move = 'X'
            Illegal = True
        else:
            color2move = 'wb'[int(Color[0])]

        castlingrights = ''
        if Vector[12*64+2]:
            castlingrights += 'K'
        if Vector[12*64+3]:
            castlingrights += 'Q'
        if Vector[12*64+4]:
            castlingrights += 'k'
        if Vector[12*64+5]:
            castlingrights += 'q'
        if len(castlingrights) is 0:
            castlingrights = '-'

        EnPassant = np.where(Vector[12*64+6:12*64+6+16])[0]
        if len(EnPassant) > 1:
            enpassant = 'X'
            Illegal = True
        elif len(EnPassant) is 0:
            enpassant = '-'
        else:
            for it in range(len(EnPassantList)):
                if Vector[12*64+6+it]:
                    enpassant = EnPassantList[it]

        halfmoveclock = int(Vector[12*64+6+16])
        fullmovenumber = int(Vector[12*64+6+16+1])

        board_asString3 += '\n'
        board_asString3 += color2move + ' ' + castlingrights + ' ' + enpassant + ' ' + str(halfmoveclock) + ' ' + str(fullmovenumber)
    return board_asString3,Illegal

if __name__ is '__main__':
    Board = chess.Board()
    for i in range(10):
        best_board(Board,search_depth=6)

        Vector = board2vector(Board)
        b = vector2board(Vector)
        display(b)
