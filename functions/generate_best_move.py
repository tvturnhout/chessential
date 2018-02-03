import chess.uci

engine = chess.uci.popen_engine("C:/Users/TvT/Documents/chessential/stockfish-9-win/stockfish_9_x64.exe")
engine.uci()
engine.author
'Tord Romstad, Marco Costalba and Joona Kiiski'

# Synchronous mode.
board = chess.Board("1k1r4/pp1b1R2/3q2pp/4p3/2B5/4Q3/PPP2B2/2K5 b - - 0 1")
engine.position(board)
engine.go(movetime=2000)  # Gets a tuple of bestmove and ponder move
BestMove(bestmove=Move.from_uci('d6d1'), ponder=Move.from_uci('c1d1'))