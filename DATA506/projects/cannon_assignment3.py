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
print('Using 33% holdouts with 3 folds')
print('--------------------------')

poly_fit2_array = []
poly_fit3_array = []
poly_fit4_array = []

for part in partitions:
    X_test = [X[i] for i in part]
    Y_test = [Y[i] for i in part]
    X_train = np.delete(X,[i for i in part])
    Y_train = np.delete(Y,[i for i in part])

    poly_fit_2 = np.polyfit(X_train,Y_train,2)
    poly_fit_3 = np.polyfit(X_train,Y_train,3)
    poly_fit_4 = np.polyfit(X_train,Y_train,4)

    poly_fit2_array.append(poly_fit_2)
    poly_fit3_array.append(poly_fit_3)
    poly_fit4_array.append(poly_fit_4)

poly_fit_2_avg = np.mean(poly_fit2_array, axis=0)
poly_fit_3_avg = np.mean(poly_fit3_array, axis=0)
poly_fit_4_avg = np.mean(poly_fit4_array, axis=0)


print('The total folds average of the coefficients for a 2nd order polynomial are (beginning with the highest order):')
print(poly_fit_2_avg)
print('The total folds average of the coefficients for a 3rd order polynomial are (beginning with the highest order):')
print(poly_fit_3_avg)
print('The total folds average of the coefficients for a 4th order polynomial are (beginning with the highest order):')
print(poly_fit_4_avg)
print('--------------------------')

new_y_2 = poly_fit_2_avg[0]*(new_x**2) + poly_fit_2_avg[1]*new_x + poly_fit_2_avg[2]
new_y_3 = poly_fit_3_avg[0]*(new_x**3) + poly_fit_3_avg[1]*(new_x**2) + poly_fit_3_avg[2]*new_x + poly_fit_3_avg[3]
new_y_4 = poly_fit_4_avg[0]*(new_x**4) + poly_fit_4_avg[1]*(new_x**3) + poly_fit_4_avg[2]*(new_x**2) + poly_fit_4_avg[3]*new_x + poly_fit_4_avg[4]

print('For the x values:')
print(new_x)
print('The predicted y values for a 2nd order polynomial are:')
print(new_y_2)
print('The predicted y values for a 3rd order polynomial are:')
print(new_y_3)
print('The predicted y values for a 4th order polynomial are:')
print(new_y_4)
print('--------------------------')
print('==========================\n\n')



print('==========================')
print('Q2')
print('--------------------------')
print('with a single 20% holdout:')

np.random.shuffle(data)

test_data = data[0:20]
train_data = data[21:]

all_x_test_data = test_data[:,0:3]
all_x_train_data = train_data[:,0:3]

y_test_data = test_data[:,3]
y_train_data = train_data[:,3]


model = LinearRegression()

model.fit(all_x_train_data,y_train_data)
print('r coefficients for the multiple linear model are: \n\tX1 '+str(model.coef_[0])+'\n\tX2 '+str(model.coef_[1])+'\n\tX3 '+str(model.coef_[2]))

test_vals = [0.3, 0.4, 0.1]
Yhat = model.predict([test_vals])
print('--------------------------')
print('For the x values:')
print(test_vals)
print('The predicted y value is:')
print(Yhat)
