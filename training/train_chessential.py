import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

# Generate dummy data
import numpy as np
x_train = np.random.random((3, 20))
y_train = keras.utils.to_categorical(np.random.randint(10, size=(3, 1)), num_classes=10)
y_train = [[ 1,  0,  1,  0,  1,  0,  1,  1,  0,  0],[ 1,  0,  1,  0,  0,  0,  0,  0,  0,  0],[ 0,  1,  0,  0,  1,  0,  1,  1,  0,  1]]
x_test = np.random.random((3, 20))
y_test = keras.utils.to_categorical(np.random.randint(10, size=(3, 1)), num_classes=10)
y_test = [[ 1,  0,  1,  0,  0,  0,  0,  0,  0,  0],[ 0,  0,  1,  0,  0,  1,  0,  0,  0,  0],[ 0,  1,  0,  0,  0,  0,  0,  0,  0,  0]]

print(y_test)
model = Sequential()
# Dense(64) is a fully-connected layer with 64 hidden units.
# in the first layer, you must specify the expected input data shape:
# here, 20-dimensional vectors.
model.add(Dense(64, activation='relu', input_dim=20))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='sigmoid'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='binary_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=20,
          batch_size=128)
score = model.evaluate(x_test, y_test, batch_size=128)

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")
 



# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

outcome = model.predict(x_test, batch_size=128)
for lijst in outcome:
    newlist = [int(round(x)) for x in lijst]
    print(newlist)
