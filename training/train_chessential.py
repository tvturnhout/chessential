import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
import sys
sys.path.insert(0, './../functions')
from file_reader import readdata

# Generate dummy data
import numpy as np

def third_split_list(a_list):
    third = int(len(a_list)/3)
    return a_list[:third], a_list[third:]


X, y = readdata('./../data/20180204T0021boards.h5')

x_train, x_test = third_split_list(X)
y_train, y_test = third_split_list(y)


#print(y_test)

model = Sequential()
# Dense(64) is a fully-connected layer with 64 hidden units.
# in the first layer, you must specify the expected input data shape:
# here, 20-dimensional vectors.
model.add(Dense(300, activation='relu', input_dim=len(x_train[0])))
model.add(Dropout(0.5))
model.add(Dense(300, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(y_train[0]), activation='sigmoid'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='binary_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=1000,
          batch_size=128)
score = model.evaluate(x_test, y_test, batch_size=128)

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("weights.h5")
print("Saved model to disk")
<<<<<<< HEAD




# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")
'''
outcome = model.predict(x_test, batch_size=128)
for lijst in outcome:
    newlist = [int(round(x)) for x in lijst]
    print(newlist)
=======
>>>>>>> 0ea53556ef885fa3dd8472cd958a82fce9b60532

