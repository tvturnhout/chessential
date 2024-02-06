import h5py
import numpy as np

def readdata(fname):
    h5f = h5py.File(fname, 'r')
    dsetIn = h5f["input_boards"]
    dsetOut = h5f["output_boards"]
    X = np.transpose(np.array(dsetIn))
    Y = np.transpose(np.array(dsetOut))
    return X,Y


if __name__ is '__main__':
    fname = './../data/20180204T0021boards.h5'
    X,Y = readdata(fname)
    print(X.shape)
    print(Y.shape)
#    for i in range(X.shape[0]):
#        print(' ')
#        print(' ')
#        print(Vector2String(X[i]))

