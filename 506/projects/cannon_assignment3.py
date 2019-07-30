import numpy as np
# import random
from scipy import spatial,stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures




data = np.genfromtxt('506/data/D3.csv', delimiter = ',')

X = data[:,0]
Y = data[:,3]

avg_x = np.mean(X)
avg_y = np.mean(Y)

x_c = X - avg_x
y_c = Y - avg_y

slope = np.dot(x_c,y_c)/np.dot(x_c,x_c)

intercept = avg_y - (slope * avg_x)

new_x = np.array([0.3, 0.5, 0.8])

pred_y = slope*new_x + intercept




print('==========================')
print('Q1: a)')
print('--------------------------')
print('The linear model is:')
print('y = {}x + {}'.format(slope,intercept))
print('--------------------------')
print('For the x values:')
print(new_x)
print('The predicted y values are:')
print(pred_y)
print('==========================\n\n')


print('==========================')
print('Q1: b)')




partitions = []
index = np.arange(0,100)
np.random.shuffle(index)
partitions.append(index[0:33])
partitions.append(index[34:66])
partitions.append(index[67:100])

for part in partitions:
    X_test = [X[i] for i in part]
    Y_test = [Y[i] for i in part]
    X_train = np.delete(X,[i for i in part])
    Y_train = np.delete(Y,[i for i in part])

print(np.polyfit(X_train,Y_train,2))
print(np.polyfit(X_train,Y_train,3))
print(np.polyfit(X_train,Y_train,4))


