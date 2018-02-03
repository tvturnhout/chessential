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

import chess.uci
import numpy as np
import chess


engine = chess.uci.popen_engine("./../stockfish-9-win/Windows/stockfish_9_x64.exe")
board = chess.Board()


engine.position(board)

engine.go(movetime = 10)