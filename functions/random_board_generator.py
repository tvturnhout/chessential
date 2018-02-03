from sys import stdout
import random
 
 
pieces = ["p","p","p","p","p","p","p","p","k","q","r","r","b","b","n","n",
          "P","P","P","P","P","P","P","P","K","Q","R","R","B","B","N","N"]
 
 
def check_king(brd, c, r):
    for j in range(-1, 1):
        for i in range(-1, 1):
            cc = c + i
            rr = r + j
            if -1 < cc < 8 and -1 < rr < 8:
                pc = brd[cc + rr * 8]
                if pc == "k" or pc == "K":
                    return 1
    return 0
 
 
def generate_board():
    for i in range(17):
        n = len(pieces) - 1
        while n > 0:
            pt = random.randrange(n)
            tp = pieces[n]
            pieces[n] = pieces[pt]
            pieces[pt] = tp
            n -= 1
 
    board = [0 for i in range(64)]
    while len(pieces) > 1:
        pc = pieces[0]
        pieces.pop(0)
        while 1:
            c = random.randrange(8)
            r = random.randrange(8)
            if ((r == 0 or r == 7) and (pc == "P" or pc == "p")) or ((pc == "k" or pc == "K") and 1 == check_king( board, c, r)):
                continue
            if board[c + r * 8] == 0:
                break
        board[c + r * 8] = pc
 
    return board
 
 
def start():
    brd = generate_board()
    e = 0
    for j in range(8):
        for i in range(8):
            if brd[i + j * 8] == 0:
                e += 1
            else:
                if e > 0:
                    stdout.write("{0}".format(e))
                    e = 0
                stdout.write(brd[i + j * 8])
        if e > 0:
            stdout.write("{0}".format(e))
            e = 0
        if j < 7:
            stdout.write("/")
    stdout.write(" w - - 0 1\n")
 
    for j in range (8):
        for i in range (8):
            if brd[i + j * 8] == 0:
                stdout.write(".")
            else:
                stdout.write(brd[i + j * 8])
        print()
 
 
# entry point
start()
 