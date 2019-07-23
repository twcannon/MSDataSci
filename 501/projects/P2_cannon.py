import numpy as np
from scipy import stats
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn import svm
import matplotlib.pyplot as plt
import sys
debug = True


# headers = ['burst','class','3 class','complete','duration','sig_dur','sig_asym','sig_lag','pulse pk flux','sig_pk flux','S(1+2+3)','sigS(1+2+3)','hr31 (erg)','sig hr31 (erg)','log10(dur)','asymmetry','lag','log10(p256)','log10(S)','log10(hr31)']

data = []
import csv
with open('501/data/project_two/2010 GRB pulse table.csv', newline='\n') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader)
    for row in reader:
        data.append(np.asarray(row))
data = np.asarray(data)







training_data = data[:700,:]
test_data = data[701:,:]

X1 = training_data[:,14].astype(np.float32) # log10(dur)
X2 = training_data[:,15].astype(np.float32) # asymmetry
Y = training_data[:,18].astype(np.float32) # log10(lag)
X = training_data[:,14:16].astype(np.float32) # log10(duration) and asymmetry

Y_test = test_data[:,18].astype(np.float32)
X_test = test_data[:,14:16].astype(np.float32) # log10(duration) and asymmetry







slope, intercept, r_value, p_value, std_err = stats.linregress(X1,Y)
Yhat = intercept + slope*X1
print( "Yhat = {0:0.2f} + {1:0.2f}X1".format( intercept, slope ) )
print( "r value = {0:0.2f}".format( r_value ) )
Xp = np.linspace( np.min(X1), np.max( X1 ) )
Yline = intercept + slope*Xp









# plt.figure()
# plt.plot( Xp, Yline )
# plt.title( "log10(duration) -vs- log10(lag)")
# plt.scatter( X1, Y, color='red', marker='.' )
# plt.xlabel( "log10(duration)" )
# plt.ylabel( "log10(lag)" )
# plt.show()






model = linear_model.LinearRegression()
model.fit(X,Y)
Yhat = model.predict(X_test)
print(model.coef_[0])
print(model.coef_[1])
print('r coefficients: \n\tX1 '+str(model.coef_[0])+'\n\tX2 '+str(model.coef_[0]))








MSE = mean_squared_error(Y_test, Yhat)
RMSD = np.sqrt(mean_squared_error(Y_test, Yhat))
MAE = mean_absolute_error(Y_test, Yhat)
print('MSE: {0:0.3f}'.format(MSE))
print('RMSD: {0:0.3f}'.format(RMSD))
print('MAE: {0:0.3f}'.format(MAE))







S_idx = data[:,1] == 'S'
not_S_idx = data[:,1] != 'S'

D1 = data[S_idx,:]
D2 = data[not_S_idx,:]

D1x = D1[:,14].astype(np.float32)
D2x = D2[:,14].astype(np.float32)
D1y = D1[:,18].astype(np.float32)
D2y = D2[:,18].astype(np.float32)








# plt.figure()
# plt.title( "Scatter plot [Labeled Data]")
# plt.xlabel( "log10(duration)" )
# plt.ylabel( "log10(lag)" )
# plt.scatter( D1x, D1y, color='red', marker='.', label="Short")
# plt.scatter( D2x, D2y, color='blue', marker='.', label="Long")
# plt.legend()
# plt.show()








clf = svm.SVC(kernel='linear')
clf.fit(np.dstack((data[:,14],data[:,18]))[0], S_idx)
print( 'Intercept: '+str(clf.intercept_[0]) )
print( 'Correlation coefficients: '+str(clf.coef_[0]) )


w = clf.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(-0.5, 0)
yy = a * xx - (clf.intercept_[0]) / w[1]
margin = 1 / np.sqrt(np.sum(clf.coef_ ** 2))
yy_down = yy - np.sqrt(1 + a ** 2) * margin
yy_up = yy + np.sqrt(1 + a ** 2) * margin



plt.figure()
plt.plot(xx, yy, 'k-')
plt.plot(xx, yy_down, 'k--')
plt.plot(xx, yy_up, 'k--')
plt.scatter( D1x, D1y, color='red', marker='.', label="Short")
plt.scatter( D2x, D2y, color='blue', marker='.', label="Long")
plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], marker='o',
                facecolors='none', edgecolors='black')
plt.show()
