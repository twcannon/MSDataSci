
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

my_data = np.genfromtxt('winequality-white.csv', delimiter=';', skip_header=1)
np.random.shuffle(my_data)

x, y = my_data[:,:11], my_data[:,11:12]
training_x, testing_x, training_y, testing_y = train_test_split(x, y, test_size=0.2)

training_y_one_hot = np.zeros((training_y.shape[0], 7), dtype=np.int)

for idx, el in enumerate(training_y):
    training_y_one_hot[idx][int(el)-3] = 1

    X = tf.placeholder(dtype=tf.float32)
    Y = tf.placeholder(dtype=tf.float32)

    w_tensor_first_layer = tf.Variable(tf.random_normal((11, 32)), dtype=tf.float32)
    w_tensor_second_layer = tf.Variable(tf.random_normal((32, 64)), dtype=tf.float32)
    w_tensor_third_layer = tf.Variable(tf.random_normal((64, 7)), dtype=tf.float32)

    b_tensor_first_layer = tf.Variable(tf.random_normal((1, 32)), dtype=tf.float32)
    b_tensor_second_layer = tf.Variable(tf.random_normal((1, 64)), dtype=tf.float32)
    b_tensor_third_layer = tf.Variable(tf.random_normal((1, 7)), dtype=tf.float32)

    after_layer_1 = tf.add(tf.matmul(X, w_tensor_first_layer), b_tensor_first_layer)
    after_layer_2 = tf.add(tf.matmul(after_layer_1, w_tensor_second_layer), b_tensor_second_layer)
    after_layer_3 = tf.add(tf.matmul(after_layer_2, w_tensor_third_layer), b_tensor_third_layer)

    y_hat = tf.nn.softmax(after_layer_3)
    y_hat_softmax = tf.nn.softmax(y_hat)

    loss = tf.nn.softmax_cross_entropy_with_logits(labels=training_y_one_hot, logits=after_layer_3)

    loss = tf.reduce_mean(loss)

    optimizer = tf.train.GradientDescentOptimizer(.00001).minimize(loss)
    init = tf.global_variables_initializer()

    with tf.Session() as sess:
      sess.run(init)

      for numOfIterations in range(300):
        sess.run(optimizer, feed_dict={X: training_x, Y: training_y_one_hot})
        c = sess.run(loss, feed_dict={X: training_x, Y: training_y_one_hot})
        print(c)
        print(numOfIterations, "/100")

      results = sess.run(y_hat_softmax, feed_dict={X: testing_x})
      index_of_highest_predicted = np.argmax(results, axis=1)

      for idx in range(len(testing_y)):
          print("Actual is " + str(testing_y[idx]) + ". Predicted is: " + str(index_of_highest_predicted[idx] + 3))