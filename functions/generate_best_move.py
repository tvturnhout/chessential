import chess.uci

engine = chess.uci.popen_engine("C:\\Users\\TvT\\Documents\\chessential\\stockfish-9-win\Windows\stockstockfish_9_x64.exe")

from stockfishpy.stockfishpy import *
chessEngine = Engine("C:\\Users\\TvT\\Documents\\chessential\\stockfish-9-win\Windows\stockstockfish_9_x64.exe", param={'Threads': 2, 'Ponder': 'true'})
print(chessEngine.uci())

print(chessEngine.isready())


chessEngine.ucinewgame()
chessEngine.setposition('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1')
move = chessEngine.bestmove()
print(move['bestmove'])