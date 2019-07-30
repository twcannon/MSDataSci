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
    print('--------------------------')
    print('For the 33% partition holdout:')
    print('--------------------------')
    X_test = [X[i] for i in part]
    Y_test = [Y[i] for i in part]
    X_train = np.delete(X,[i for i in part])
    Y_train = np.delete(Y,[i for i in part])

    poly_fit_2 = np.polyfit(X_train,Y_train,2)
    poly_fit_3 = np.polyfit(X_train,Y_train,3)
    poly_fit_4 = np.polyfit(X_train,Y_train,4)

    print('The coefficients for a 2nd order polynomial are:')
    print(poly_fit_2)
    print('The coefficients for a 3rd order polynomial are:')
    print(poly_fit_3)
    print('The coefficients for a 4th order polynomial are:')
    print(poly_fit_4)
    print('--------------------------')

    new_y_2 = poly_fit_2[0]*(new_x**2) + poly_fit_2[1]*new_x + poly_fit_2[2]
    new_y_3 = poly_fit_3[0]*(new_x**3) + poly_fit_3[1]*(new_x**2) + poly_fit_3[2]*new_x + poly_fit_3[3]
    new_y_4 = poly_fit_4[0]*(new_x**4) + poly_fit_4[1]*(new_x**3) + poly_fit_4[2]*(new_x**2) + poly_fit_4[3]*new_x + poly_fit_4[4]
    print('For the x values:')
    print(new_x)
    print('The predicted y values for a 2nd order polynomial are:')
    print(new_y_2)
    print('The predicted y values for a 3rd order polynomial are:')
    print(new_y_3)
    print('The predicted y values for a 4th order polynomial are:')
    print(new_y_4)
    print('--------------------------\n\n')
print('==========================\n\n')

all_x_data = data[:,0:3]
all_x_test = [all_x_data[i] for i in part]
Y_test = [Y[i] for i in part]
all_x_train = np.delete(all_x_data,[i for i in part])
Y_train = np.delete(Y,[i for i in part])

model = LinearRegression()
print(all_x_train)
print(Y_train)
model.fit(all_x_train,Y_train)
Yhat = model.predict([all_x_test])
print(model.coef_[0])
print(model.coef_[1])
print(model.coef_[2])
print('r coefficients: \n\tX1 '+str(model.coef_[0])+'\n\tX2 '+str(model.coef_[1])+'\n\tX3 '+str(model.coef_[2]))
