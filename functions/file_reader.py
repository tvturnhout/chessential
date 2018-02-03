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

import h5py
import numpy as np
from vectorizer import Vector2String

def ReadData(fname):
    h5f = h5py.File(fname, 'r')
    dsetIn = h5f["input_boards"]
    dsetOut = h5f["output_boards"]
    X = np.transpose(np.array(dsetIn))
    Y = np.transpose(np.array(dsetOut))
    return X,Y


if __name__ is '__main__':
    fname = 'Data/20180204T0000boards.h5'
    X,Y = ReadData(fname)
    print(X.shape)
    print(Y.shape)
    for i in range(X.shape[0]):
        print(' ')
        print(' ')
        print(Vector2String(X[i]))

