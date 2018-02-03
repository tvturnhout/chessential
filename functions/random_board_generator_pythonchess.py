import chess
import random

board = chess.Board()
legal_moves = board.legal_moves
move = random.choice(legal_moves)

print (move)
