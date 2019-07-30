import numpy as np
from scipy import spatial,stats
import matplotlib.pyplot as plt




data = np.genfromtxt('506/data/D3.csv', delimiter = ',')

# print(data)

X = data[:,0]
Y = data[:,3]

# print(X)
# print(Y)

avg_x = np.mean(X)
avg_y = np.mean(Y)

# print(avg_x)
# print(avg_y)

x_c = X - avg_x
y_c = Y - avg_y

# print(x_c)
# print(y_c)

slope = np.dot(x_c,y_c)/np.dot(x_c,x_c)

intercept = avg_y - (slope * avg_x)
print('==========================')
print('Q1: a)')
print('---------------------------')
print('The linear model is:')
print('y = {}x + {}'.format(slope,intercept))
print('==========================')



slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
print(slope)
print(intercept)
print(r_value)
print(p_value)
print(std_err)