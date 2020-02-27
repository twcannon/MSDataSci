import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import warnings  
with warnings.catch_warnings():  
    warnings.filterwarnings("ignore",category=FutureWarning)
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.keras.preprocessing.text import Tokenizer

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
# print(x_train, y_train)
# print('===============')
# print(x_test, y_test)

x_test = x_test.astype(dtype=int)
x_train = x_train.astype(dtype=int)



# myTest = x_test[9]

# best_diff = 100000000
# closest_image = None

# for curr_index in range(len(x_test)):
# 	diff = (abs(myTest-x_train[curr_index]).sum())
# 	if diff < best_diff:
# 		best_diff = diff
# 		closest_image = x_train[curr_index]




myTest = x_test[9]

num_of_correct = 0

for curr_test_index in range(100):
	best_diff = 10000000000
	best_label = None
	for curr_index in range(len(x_train)):
		diff = (abs(x_test[curr_test_index]-x_train[curr_index]).sum())
		if diff < best_diff:
			best_diff = diff
			best_label = y_train[curr_index]
	if best_label == y_test[curr_test_index]:
		num_of_correct += 1

print(num_of_correct)
# f, axarr = plt.subplots(1,2)
# axarr[0].imshow(myTest, cmap='gray')
# axarr[1].imshow(closest_image, cmap='gray')
# plt.show()