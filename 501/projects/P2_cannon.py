import numpy as np
from scipy import stats
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import sys
debug = True


headers = ['burst','class','3 class','complete','duration','sig_dur','sig_asym','sig_lag','pulse pk flux','sig_pk flux','S(1+2+3)','sigS(1+2+3)','hr31 (erg)','sig hr31 (erg)','log10(dur)','asymmetry','lag','log10(p256)','log10(S)','log10(hr31)']

data = np.genfromtxt('501/data/project_two/2010 GRB pulse table.csv', delimiter = ',',skip_header=True)





training_data = data[:700,:]
test_data = data[701:,:]

X1 = training_data[:,14] # log10(dur)
X2 = training_data[:,15] # asymmetry
Y = training_data[:,18] # log10(lag)
X = training_data[:,14:16] # log10(duration) and asymmetry

Y_test = test_data[:,18]
X_test = test_data[:,14:16] # log10(duration) and asymmetry







slope, intercept, r_value, p_value, std_err = stats.linregress(X1,Y)
Yhat = intercept + slope*X1
print( "Yhat = {0:0.2f} + {1:0.2f}X1".format( intercept, slope ) )
print( "r value = {0:0.2f}".format( r_value ) )
Xp = np.linspace( np.min(X1), np.max( X1 ) )
Yline = intercept + slope*Xp






plt.figure()
plt.plot( Xp, Yline )
plt.title( "log10(duration) -vs- log10(lag)")
plt.scatter( X1, Y, color='red', marker='.' )
plt.show()






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






