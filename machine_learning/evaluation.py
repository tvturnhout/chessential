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
from vectorize import vector2board, vector2string, board2vector
from IPython.display import SVG
import chess
import time


def legal_move(board_in,board_out):
    """
    Name:
        legal_move
    Description:
        This functions verifies whether board_pred can be obtained by
        performing a legal move on board_in and returns said legal move
        (or None).
    Input:
        board_in:       input board for the legal move check
                        chess.Board or vector representation
        board_out:      output board for the legal move check
                        chess.Board or vector representation
    Output:
        legalmove:     which legal move links the two boards, if any.
    """
    if not type(board_in) is chess.Board\
        and hasattr(board_in,'__iter__'):
        board_in = vector2board(board_in)
    if not type(board_out) is chess.Board\
        and hasattr(board_out,'__iter__'):
        board_out = vector2board(board_out)
    possible_moves = []
    possible_outcomes = []
    for move in  board_in.legal_moves:
        possible_moves.append(move)
        board = board_in.copy()
        board.push(move)
        possible_outcomes.append(board)
    i = 0
    legal = []
    for i in range(len(possible_outcomes)):
        legal.append(str(possible_outcomes[i]) == str(board_out))
    legalmovesfound = np.where(legal)[0]
    if len(legalmovesfound) > 0:
        legalmove = possible_moves[legalmovesfound[0]]
    else:
        legalmove = None
    return legalmove



if __name__ is '__main__':
    """
    Check predictions on dataset
    """
    debug_illegal_predictions = False
    print_moves = False

    X, y = readdata('./../data/20180209T2142boards.h5')

    predicted_boards = predict(X)

    start = time.time()
    legal_counter = 0
    for i in range(len(predicted_boards)):
        board_pred = predicted_boards[i]
        board_in = X[i]
        move = legal_move(board_in,board_pred)
        if print_moves:
            print('Legal move: {}'.format(move))
        if move is None and debug_illegal_predictions:
            print('Board in:\n-------------------')
            display(vector2board(board_in))
            print('Board predicted:\n-------------------')
            display(vector2board(board_pred))
            ans = input("Press Enter to continue, 'quit' to stop debugging...")
            if ans == 'quit':
                debug_illegal_predictions = False
        elif not move is None:
            legal_counter = legal_counter + 1
    end = time.time()
    print('Verification time per move: {0:0.5f}sec'.format((end-start)/len(predicted_boards)))



    print('Percentage of legal moves: {}%'.format(float(legal_counter)/float(len(predicted_boards))*100))


    """
    Check if all legal moves can be detected from all legal outcomes of start
    situation.
    """
    print('Legal moves detected from all legal outcomes of start situation:')
    board = chess.Board()
    potential_moves = []
    potential_outcomes = []
    for move in board.legal_moves:
        potential_moves.append(move)
        b = board.copy()
        b.push(move)
        potential_outcomes.append(b)
    moves = [legal_move(board,potential_outcomes[i]) for i in range(len(potential_outcomes)) ]
    print(moves)