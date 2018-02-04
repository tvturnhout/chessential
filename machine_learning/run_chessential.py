import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
import numpy as np
from keras.models import model_from_json
import chess
import sys
sys.path.insert(0, './../functions')

def predict(X_in):
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("weights.h5")
    print("Loaded model from disk")

    outcome = loaded_model.predict(X_in, batch_size=128)

    parsed_outcome = []
    for lijst in outcome:
        newlist = [int(round(x)) for x in lijst]
        parsed_outcome.append(newlist)

    return(parsed_outcome)

