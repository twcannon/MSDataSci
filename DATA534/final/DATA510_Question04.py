

# EXAMPLE OUTPUT

'''######################
            .
            .
            .
            .
Epoch 2998/3000
162/162 [==============================] - 0s 271us/sample - loss: 0.0517 - val_loss: 55.8079
Epoch 2999/3000
162/162 [==============================] - 0s 249us/sample - loss: 0.0421 - val_loss: 55.7748
Epoch 3000/3000
162/162 [==============================] - 0s 257us/sample - loss: 0.0533 - val_loss: 55.7304
Predicted: [0 1 0]. Actual: [0 1 0]
Predicted: [0 1 0]. Actual: [0 0 1]
Predicted: [1 0 0]. Actual: [1 0 0]
Predicted: [0 1 0]. Actual: [0 0 1]
Predicted: [1 0 0]. Actual: [1 0 0]
Predicted: [0 1 0]. Actual: [0 1 0]
Predicted: [0 1 0]. Actual: [0 1 0]
Predicted: [0 1 0]. Actual: [1 0 0]
Predicted: [0 1 0]. Actual: [1 0 0]
Predicted: [0 1 0]. Actual: [0 0 1]
Predicted: [0 1 0]. Actual: [0 0 1]
Predicted: [1 0 0]. Actual: [1 0 0]
Predicted: [0 1 0]. Actual: [0 0 1]
Predicted: [1 0 0]. Actual: [1 0 0]
Predicted: [0 1 0]. Actual: [0 0 1]
Predicted: [0 0 1]. Actual: [1 0 0]
Predicted: [0 0 1]. Actual: [1 0 0]
Predicted: [0 1 0]. Actual: [0 0 1]
Predicted: [1 0 0]. Actual: [1 0 0]
Predicted: [0 0 1]. Actual: [1 0 0]
Predicted: [1 0 0]. Actual: [1 0 0]
Predicted: [1 0 0]. Actual: [1 0 0]
Predicted: [0 1 0]. Actual: [0 0 1]
Predicted: [0 0 1]. Actual: [0 0 1]
Predicted: [1 0 0]. Actual: [1 0 0]
Predicted: [0 1 0]. Actual: [0 0 1]
12/26 Correct
'''######################


import numpy as np
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Dense

training_input = np.load('training_input.npy')
training_output = np.load('training_output.npy')
validation_input = np.load('validation_input.npy')
validation_output = np.load('validation_output.npy')


model = tf.keras.models.Sequential()
drop_out = 0.2
iterations = 5000

def main():

    model.add(tf.keras.layers.LSTM(units=60, activation='relu', input_shape=(6, 2)))
    model.add(tf.keras.layers.Dropout(drop_out))

    model.add(tf.keras.layers.Dense(units=40, activation ='relu'))
    model.add(tf.keras.layers.Dropout(drop_out))

    model.add(tf.keras.layers.Dense(units=3))
    model.add(tf.keras.layers.Dropout(drop_out))

    model.add(Dense(units=3, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam')

    monitor = EarlyStopping(monitor='val_loss', min_delta=0.01,patience=iterations,
                            mode='auto', restore_best_weights=True)

    model.fit(training_input, training_output,
              validation_data=(validation_input, validation_output),
              batch_size=162, callbacks=[monitor], epochs=iterations)

    predicted = model.predict(validation_input)
    predicted = np.reshape(predicted, (len(predicted), 3)).tolist()
    
    num_correct = 0
    for idx, p in enumerate(predicted):
        zeros = np.array([0]*3)
        p = np.array(p).astype(float)
        zeros[np.argmax(p)] = 1
        if str(zeros) == str(validation_output[idx]):
            num_correct+=1
        print("Predicted: " + str(zeros) + ". Actual: " + str(validation_output[idx]))
    print(str(num_correct)+'/'+str(len(validation_output))+' Correct')

if __name__ == "__main__":
    main()