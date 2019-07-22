import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt
import sys
debug = True



headers = ['burst','class','3 class','complete','duration','sig_dur','sig_asym','sig_lag','pulse pk flux','sig_pk flux','S(1+2+3)','sigS(1+2+3)','hr31 (erg)','sig hr31 (erg)','log10(dur)','asymmetry','lag','log10(p256)','log10(S)','log10(hr31)']
# data_types = [('burst','S5'),('class','S5'),('3 class','S5'),('complete','S5'),('duration','f8'),('sig_dur','f8'),('sig_asym','f8'),('sig_lag','f8'),('pulse pk flux','f8'),('sig_pk flux','f8'),('S(1+2+3)','f8'),('sigS(1+2+3)','f8'),('hr31 (erg)','f8'),('sig hr31 (erg)','f8'),('log10(dur)','f8'),('asymmetry','f8'),('lag','f8'),('log10(p256)','f8'),('log10(S)','f8'),('log10(hr31)','f8')]

# data_types = 'S5,S5,S5,S5,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8,f8'

data = np.genfromtxt('501/data/project_two/2010 GRB pulse table.csv', delimiter = ',',skip_header=True)
# data = np.matrix(data)
print(data)
print(type(data))
print(type(data[0]))

# for row in range(0,len(data)):
#     if data[row,6]<-0.2:
#         print('-------------'+str(row)+'-------------')


# Y is the dependent variable
# X is the independent variable 
def ols_regression( Y, X ):
    
    # n = number of samples
    n = np.size( Y, 0 )
    
    # make things a bit easier
    SUM_XY = np.sum( np.multiply( X, Y ) )
    SUMX_SUMY = np.sum( X ) * np.sum( Y )
    SUM_X2 = np.sum( np.multiply( X, X ) )
    SUM_Y2 = np.sum( np.multiply( Y, Y ) )
    SUM_X_2 = np.sum( X )**2
    SUM_Y_2 = np.sum( Y )**2
    
    #mean of X and Y
    Xbar = np.mean( X )
    Ybar = np.mean( Y )
    
    # estimate the regression coefficents
    b = ( ( n * SUM_XY ) - ( SUMX_SUMY ) ) / ( ( n* SUM_X2) - SUM_X_2 )
    a = Ybar - b*Xbar
    
    r = ( SUM_XY - (1/n)*SUMX_SUMY ) / np.sqrt( ( SUM_X2 - (1/n)*SUM_X_2 )*( SUM_Y2 - (1/n)*SUM_Y_2 ) )

    return a,b,r

# print(np.size(data))
# print(np.shape(data))
# idx = data[:,1] == 'S'
# data = data[idx,:]

# print(np.size(data))

X = data[:,15] # runs\n",
Y = data[:,19] # wins\n",
# Y = data[:,18] # wins\n",
# Y = data[:,14] # wins\n",
a,b,r = ols_regression( Y, X )
# Yhat = a + bX\n",
print( "Yhat = {0:0.2f} + {1:0.2f}X".format( a, b ) )
print( "r = {0:0.2f}".format( r ) )
Xp = np.linspace( np.min(X), np.max( X ) )
Yhat = a + b*Xp
plt.figure()
plt.plot( Xp, Yhat )
plt.title( "X -vs- Y")
plt.scatter( X, Y, color='red', marker='.' )
plt.show()