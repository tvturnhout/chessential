import chess
import random



board = chess.Board()
print(board)

boards = []
i = 0
while not i > 50 or board.is_game_over() or board.is_insufficient_material() or board.is_stalemate() or board.is_seventyfive_moves():

    legal_moves = board.legal_moves
    potential_moves = []
    for item in legal_moves:
        potential_moves.append(item)

    i = i + 1 
    move = random.choice(potential_moves)
    board.push(move)
    boards.append(board)
    print(move)
    #print(board)
    print(len(boards))

outF = open("myOutFile.txt", "w")
for line in boards:
  outF.write(line)
  outF.write("\n")
outF.close()



