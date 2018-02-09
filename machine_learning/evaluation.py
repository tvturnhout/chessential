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
    Comment:
        At this point this function does not check castling rights,
        whose turn it is, the counters and any en passant rights.
        This can easily be implemented later by using the board2vector and
        vector2string method subsequently instead of the str() method now used
        to compare. This current method is however less strict and can be used
        in an early stage of the neural net.
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


def play_against_nn():
    board = chess.Board()
    while not board.is_game_over() \
            and not board.is_insufficient_material() \
            and not board.is_stalemate() \
            and not board.is_fivefold_repetition() \
            and not board.is_seventyfive_moves():
        print('Board before your move:\n'+22*'-')
        display(board)
        i = 0
        moves = []
        for move in board.legal_moves:
            moves.append(move)
        for i in range(0,len(moves),3):
            rem = min(len(moves)-i-1,2)
            string = '{}:  {}'
            args = (i,moves[i])
            for it in range(rem):
                string += '\t\t{}:  {}'
                args += (i+1+it,moves[i+1+it])
            print(string.format(*args))
        ans = input("Enter the move you want to enter (or 'quit' to stop):\n")
        if ans == 'quit':
            return
        board.push(moves[int(ans)])
        print('Board after your move:\n'+22*'-')
        display(board)
        board = vector2board(predict(  np.array([board2vector(board),],dtype='float64')  )[0] )


if __name__ is '__main__':
    check_data_file = False
    check_start_moves = False
    play = True

    """
    Check predictions on dataset
    """
    if check_data_file:
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
    if check_start_moves:
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

    if play:
        play_against_nn()