

# EXAMPLE OUTPUT
# learning_rate=.001
# num_iterations=500

'''######################
489/500 0.40715414
490/500 0.4065323
491/500 0.40591168
492/500 0.40529436
493/500 0.4046798
494/500 0.40406793
495/500 0.40346035
496/500 0.40285802
497/500 0.4022586
498/500 0.4016623
499/500 0.40107042
Num of correct is: 851 out of 1000
'''######################


import numpy as np
import tensorflow.compat.v1 as tf
from tensorflow.keras.datasets import mnist
tf.disable_v2_behavior()


learning_rate=.001
num_iterations=500




def main():

    train_size=5000
    test_size=1000
    stddev=0.05

    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = np.reshape(x_train, (x_train.shape[0] ,28, 28, 1))[:train_size]
    x_test = np.reshape(x_test, (x_test.shape[0] ,28, 28, 1))[:test_size]
    y_train = y_train[:train_size]
    y_test = y_test[:test_size]

    y_train_one = np.zeros((y_train.shape[0], 10), dtype=np.int)
    for idx, el in enumerate(y_train):
        y_train_one[idx][el] = 1
    y_train_one = y_train_one.astype('float32')

    y_test_one = np.zeros((y_test.shape[0], 10), dtype=np.int)
    for idx, el in enumerate(y_test):
        y_test_one[idx][el] = 1


    training_x_placeholder = tf.placeholder(dtype=tf.float32, shape=(None, 28, 28, 1))
    training_y_placeholder = tf.placeholder(dtype=tf.float32)


    first_layer = tf.nn.conv2d(input=training_x_placeholder,
                                  filter=tf.Variable(tf.random_normal([5, 5, 1, 16], stddev=stddev)),
                                  strides=[1, 1, 1, 1],padding='SAME')
    print("Size after convolving first layer:", first_layer.get_shape())


    first_layer_post_pool = tf.nn.max_pool(value=first_layer,
                                            ksize=[1, 2, 2, 1],
                                            strides=[1, 2, 2, 1],padding='SAME')
    first_layer_post_pool = tf.nn.relu(first_layer_post_pool)
    print("Size after pooling of first layer:", first_layer_post_pool.get_shape())


    second_layer = tf.nn.conv2d(input=first_layer_post_pool,
                                   filter=tf.Variable(tf.random_normal([5, 5, 16, 8], stddev=stddev)),
                                   strides=[1, 1, 1, 1],padding='SAME')
    print("Size after convolving second layer:", second_layer.get_shape())


    second_layer_post_pool = tf.nn.max_pool(value=second_layer,
                                                 ksize=[1, 2, 2, 1],
                                                 strides=[1, 2, 2, 1],padding='SAME')
    second_layer_post_pool = tf.nn.relu(second_layer_post_pool)
    print("Size after pooling of second layer:", second_layer_post_pool.get_shape())


    layer_flat = tf.reshape(second_layer_post_pool, (-1, 7 * 7 * 8))
    print("The shape after flattening is:", layer_flat.get_shape())


    weights_after_cnn_l1 = tf.Variable(tf.random_normal((392, 32), stddev=stddev))
    bias_after_cnn_l1 = tf.Variable(tf.random_normal((1, 32), stddev=stddev))
    out_layer = tf.matmul(layer_flat, weights_after_cnn_l1) + bias_after_cnn_l1
    out_layer = tf.nn.relu(out_layer)


    weights_after_cnn_l2 = tf.Variable(tf.random_normal((32, 32), stddev=stddev))
    bias_after_cnn_l2 = tf.Variable(tf.random_normal((1, 32), stddev=stddev))
    out_layer = tf.matmul(out_layer, weights_after_cnn_l2) + bias_after_cnn_l2
    out_layer = tf.nn.relu(out_layer)


    weights_after_cnn_l3 = tf.Variable(tf.random_normal((32, 10), stddev=stddev))
    bias_after_cnn_l3 = tf.Variable(tf.random_normal((1, 10), stddev=stddev))
    out_layer = tf.matmul(out_layer, weights_after_cnn_l3) + bias_after_cnn_l3


    predicted = tf.nn.softmax(out_layer)

    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=out_layer,labels=y_train_one))

    optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)

    init = tf.global_variables_initializer()


    with tf.Session() as sess:
        sess.run(init)
        for el in range(num_iterations):
            sess.run(optimizer, feed_dict={training_x_placeholder: x_train,
                                           training_y_placeholder: y_train_one})
            c = sess.run(loss, feed_dict={training_x_placeholder: x_train,
                                          training_y_placeholder: y_train_one})
            print(str(el)+"/"+str(num_iterations),c)


        res = sess.run(predicted, feed_dict={training_x_placeholder: x_test})
        res = np.argmax(res, axis=1)
        # print("Result is: ",res)
        # print("Y Test Actual:",y_test,'\n')
        

        num_correct = 0
        for idx, el in enumerate(y_test):
            if el == res[idx]:
                num_correct += 1
        print("Num of correct is: " + str(num_correct) + " out of "+str(test_size))



if __name__ == "__main__":
    main()