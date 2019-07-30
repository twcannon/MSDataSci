import numpy as np
from scipy import spatial,stats
import matplotlib.pyplot as plt




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
print('==========================')
