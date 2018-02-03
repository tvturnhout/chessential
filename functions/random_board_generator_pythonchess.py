import chess
import random



board = chess.Board()
print(board)

legal_moves = board.legal_moves
potential_moves = []
for item in legal_moves:
    potential_moves.append(item)

move = random.choice(potential_moves)
print(move)
board.push(move)
print(board)
