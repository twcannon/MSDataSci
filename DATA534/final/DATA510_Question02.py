# For this question, you will be implementing a neural net to predict the quality of wine
#
# The feature are:
#       Fixed acidity.
#       Volatile acidity.
#       Citric acid.
#       Residual sugar.
#       Chlorides.
#       Free sulfur dioxide.
#       Total sulfur dioxide.
#       Density.
#       pH.
#       Sulphates.
#       Alcohol.
#       Quality (score between 3 and 9).
#
# This problem can be framed as a regression or as a classification problem; for this question, we'll treat it as a
#   classification problem
#
# Here's the architecture of the neural net:
#       Input layer is 11 nodes (the dimension of each input is 11; see above)
#       First hidden layer will be 32 nodes (no activation function)
#       Second hidden layer will be 64 nodes (no activation function)
#       Output layer will contain 7 nodes (one-hot encoding of values from 3 to 9)
#
#   To learn more about the dataset, you can visit:
#       https://machinelearningmastery.com/standard-machine-learning-datasets/
#
#   The first thing you'll need to do is load the file into a numpy array; one option would be to use 'genfromtxt':
#       your_array = np.genfromtxt('file_name.csv', delimiter=';', skip_header=1) (already done)
#
#   Shuffle the rows in the numpy array:
#       np.random.shuffle(your_array) (already done)
#
#   Split it into training (80%) and testing (20%)
#
#   Convert the training_y to one-hot encoding (already done for you)
#
#   Define your placeholders and Variables (you need to do that)
#
#
#
import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

my_data = np.genfromtxt('winequality-white.csv', delimiter=';', skip_header=1)
np.random.shuffle(my_data)
print(my_data)

#training_x = here, assign the first 80% of rows, all columns except the last one
#training_y = here, assign the first 80% of rows, only last column

# This code will convert the training_y into its one-hot encoding representation
#
training_y_one = np.zeros((training_y.shape[0], 7), dtype=np.int)
for idx, el in enumerate(training_y):
    # Here, we subtract 3 because we would want to shift the values:
    #       from 3 to 9
    #           to
    #       from 0 to 6
    #
    training_y_one[idx][int(el)-3] = 1

#testing_x = here, assign the last 20% of rows, all columns except the last one
#testing_y = here, assign the last 20% of rows, only last column

# Create the placeholders for X and Y

# Create the weights variables for the first hidden layer
# Create the bias variable for the first hidden layer
# Make sure that you initialize the weights to random values (you can use np.random.normal())

# Create the weights variables for the second hidden layer
# Create the bias variable for the second hidden layer
# Make sure that you initialize the weights to random values (you can use np.random.normal())

# Create the weights variables for the output layer
# Create the bias variable for the output layer
# Make sure that you initialize the weights to random values (you can use np.random.normal())

# Do the matrix multiplications plus the bias:
#       yHat = input * hidden1 + bias (modify the code so that it does matmul using tf)
#       yHat = yHat * hidden2 + bias (modify the code so that it does matmul using tf)
#       yHat = yHat * output + bias(modify the code so that it does matmul using tf)
#

# This will be used when we test our testing dataset (uncomment later)
# Recall that 'softmax_cross_entropy_with_logits' does that before it calculates the loss, which means that
#   you don't want to feed yHatSoftmax into 'softmax_cross_entropy_with_logits'
#
# yHatSoftmax = tf.nn.softmax(yHat)

# Now, you would have to do the loss, which uses the 'softmax_cross_entropy_with_logits'
#       Refer to code we've written before

# Then, you would get the mean of that using 'reduce_mean' (also in previous code)

# Define the optimizer (which uses gradient descent) and pick a good learning rate

# init = tf.global_variables_initializer()

# with tf.Session() as sess:
#     sess.run(init)
#     for numOfIterations in range(<choose epochs here>):
#         # Here, write code to run (sess.run) the optimizer and provide the correct feed_dict values
#         # Here, write code to run (sess.run) the loss and print that (to see the loss going down)


#     # You can use the following code to display the results from the testing subset
#     #
#     resultTF = sess.run(yHatSoftmax, feed_dict={X: testing_x})
#     indexOfHighestPredicted = np.argmax(resultTF, axis=1)

#     # Displaying the results
#     #
#     for idx in range(len(testing_y)):
#         # We add 3 because we need to shift the values back
#         #
#         print("Actual is " + str(testing_y[idx]) + ". Predicted is: " + str(indexOfHighestPredicted[idx] + 3))
