

# EXAMPLE OUTPUT

'''######################
            .
            .
            .
            .
Predicted is: 6. Actual is 6
Predicted is: 7. Actual is 6
Predicted is: 6. Actual is 5
Predicted is: 6. Actual is 5
Predicted is: 6. Actual is 6
Predicted is: 6. Actual is 5
Predicted is: 6. Actual is 5
Predicted is: 6. Actual is 6
Predicted is: 7. Actual is 5
Predicted is: 6. Actual is 6
Predicted is: 6. Actual is 6
Predicted is: 7. Actual is 6
413/980 Correct
'''######################



import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

my_data = np.genfromtxt('winequality-white.csv', delimiter=';', skip_header=1)
np.random.shuffle(my_data)

iterations = 10000
learning_rate = .000005


def main():

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

    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)

        for numOfIterations in range(iterations):
            sess.run(optimizer, feed_dict={X: training_x, Y: training_y_one_hot})
            c = sess.run(loss, feed_dict={X: training_x, Y: training_y_one_hot})
            print('iteration',numOfIterations, "/"+str(iterations),'| loss',c)

        results = sess.run(y_hat_softmax, feed_dict={X: testing_x})
        index_of_highest_predicted = np.argmax(results, axis=1)

        num_correct = 0
        for idx in range(len(testing_y)):
            pred = int(index_of_highest_predicted[idx] + 3)
            act  = int(testing_y[idx][0])
            if pred == act:
                num_correct +=1
            print("Predicted is: " + str(pred) + ". Actual is " + str(act))
        print(str(num_correct)+'/'+str(len(testing_y))+' Correct')


if __name__ == "__main__":
    main()