# -----------------------
# Helper functions
# -----------------------

import numpy as np

def eucdist( v1, v2 ):
    return np.linalg.norm( v1 - v2 )

def ppv( cm ):
    return ( cm[0,0] / ( np.sum( cm[0,:] ) ) )

def npv( cm ):
    return ( cm[1,1] / ( np.sum( cm[1,:] ) ) ) 

def sensitivity( cm ):
    return ( cm[0,0] / ( np.sum( cm[:,0] ) ) ) 

def specificity( cm ):
    return ( cm[1,1] / ( np.sum( cm[:,1] ) ) ) 

def f1( cm ):
    return ( 2 * ( ( ppv( cm ) * sensitivity( cm ) ) / (ppv( cm ) + sensitivity( cm ) ) ) )