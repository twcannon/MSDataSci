# For this question, you will be implementing an RNN to predict the stock data
#
# The data has already been prepared for you, and all you have to do is load the input and output
#   (code for that already written)
#
# Details provided below
#
import numpy as np
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Dense

# Use this to train your model
training_input = np.load('training_input.npy')
training_output = np.load('training_output.npy')
print(training_input.shape)
print(training_output.shape)

# Use this to set an early stopping
validation_input = np.load('validation_input.npy')
validation_output = np.load('validation_output.npy')

# Create your architecture here

# input, output = training_input, training_output
model = tf.keras.models.Sequential()

# The first layer is a LSTM RNN layer of 60 nodes, followed by a 'relu' activation function
# def main():
model.add(tf.keras.layers.LSTM(units=60, activation='relu',
                               input_shape=(6, 2)))

# Give the first layer a dropout rate of .2
model.add(tf.keras.layers.Dropout(0.2))

# The second layer is a traditional fully connected neural net layer of 40 nodes, followed by a 'relu' function
model.add(tf.keras.layers.Dense(units=40, activation ='relu'))
model.add(tf.keras.layers.Dropout(0.2))

# Give the second layer a dropout rate of .2
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(units=3))

# The output layer contains 3 nodes; use 'softmax' activation function since the labels are one-hot--encoded
model.add(Dense(units=3, activation='softmax'))

# Use 'adam' optimizer with 'categorical_crossentropy' loss function
model.compile(loss='categorical_crossentropy',
              optimizer='adam')

# Create an early stopping monitor (see code we've written together). You can use same arguments used previously
monitor = EarlyStopping(monitor='val_loss',
                        min_delta=1e-3,
                        patience=10,
                        mode='auto',
                        restore_best_weights=True)

# Call the fit method and pass the training and validation data, and pass the 'monitor' as a callback funciton
#   (again, refer to the code we've written on Tuesday last week)
model.fit(training_input,
          training_output,
          validation_data=(validation_input, validation_output),
          batch_size=162, callbacks=[monitor],
          epochs=200)

predicted = model.predict(validation_input)
print(predicted.shape)
print(len(predicted))
predicted = np.reshape(predicted, (len(predicted), 3)).tolist()
for idx, p in enumerate(predicted):
    print("Predicted: " + str(p) + ". Actual: " + str(validation_output[idx]))
