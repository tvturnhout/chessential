import chess.uci
import numpy as np
import chess

def best_board(input_board,search_depth):

    engine = chess.uci.popen_engine("./../stockfish-9-win/Windows/stockfish_9_x64.exe")
    board = input_board
    engine.position(board)
    board.push(engine.go(ponder=False , depth=search_depth)[0])
    engine.quit()

    return(board)

