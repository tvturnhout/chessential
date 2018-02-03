# -*- coding: utf-8 -*-
"""
Created on %(date)s
@author: %(username)s
"""
#%%%============================================================================
# PROGRAM METADATA
#===============================================================================
__Author__ = "Janssenswillen"
__Customer__ =  ""
__Project__ =  ""
__Purpose__ =  ""
__date__ = '%(date)s'
__version__ = '0.1'

#%%%============================================================================
# IMPORT STATEMENTS
#===============================================================================
#import numpy as np
#from visual import *  # IMPORTS NumPy.*, SciPy.*, and Visual objects (sphere, box, etc.)
#import matplotlib.pyplot as plt  # plt.plot(x,y)  plt.show()
#from pylab import *  # IMPORTS NumPy.*, SciPy.*, and matplotlib.*
#import os  # os.walk(basedir) FOR GETTING DIR STRUCTURE
#import pickle  # pickle.load(fromfile)  pickle.dump(data, tofile)
#import xlwt
#from tkFileDialog import askopenfilename, askopenfile
#from collections import namedtuple
#from ctypes import *
#import glob
#import random
#import sympy
#%%%============================================================================

import chess
import time
import numpy as np

PossibleEntries = '.prnbqkPRNBQK'

def Board2Vector(Board):
    board_asString0 = str(Board)
    board_asString = board_asString0.replace(" ", "")
    board_asString = board_asString.replace('\n', "")
    board_asvector = np.zeros(13*64)
    for b in range(len(board_asString)):
        piece = board_asString[b]
        for it in range(len(PossibleEntries)):
            board_asvector[b*13+it] = int(piece is PossibleEntries[it])
    return board_asvector

def Vector2String(Vector):
    board_asString2 = ''
    for it in range(0,len(Vector),len(PossibleEntries)):
        board_asString2 += PossibleEntries[int(np.where(Vector[it:it + 13])[0])]
    board_asString = board_asString2[0]
    for it in range(1,len(board_asString2)):
        if it % 8>0:
            board_asString +=  ' ' + board_asString2[it]
        else:
            board_asString +=  '\n' + board_asString2[it]
    return board_asString

if __name__ is '__main__':
    Board = chess.Board()
    start = time.time()
    number = 10000
    for i in range(number):
        Vector = Board2Vector(Board)
    end = time.time()
    print('Took me {} ms per board'.format((end-start)/number*1e3))

    start = time.time()
    for i in range(number):
        String = Vector2String(Vector)
    end = time.time()
    print('Took me {} ms per board'.format((end-start)/number*1e3))



