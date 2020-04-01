import mpfit
# import numpy.oldnumeric as Numeric
from burst import Burst
import numpy as np
import matplotlib.pyplot as plt
import sys


# 00143: Norris Fit
out_file = '/home/thomas/git/MSDataSci/Thesis/out_files/00143_b536_3_0.out'
burst_file = './sample_data/cat64ms.00143'

burst = Burst(burst_file)
burst.parse_batse_file()

data       = burst.burst_data
burst_meta = burst.header_data 

four_channel_data = np.sum(data, axis=1)
trig  = burst_meta['trig#']
nlasc = burst_meta['nlasc']
npts  = burst_meta['npts']

bg_height = 1047.2220
bg_slope = 0.025935641
start = 44.965676
ampl = 2823.6814
tau1 = 4.1735936
tau2 = 2.2154609
taupk = 48.006471

time = (np.linspace((-nlasc), (npts-nlasc),num=npts)*0.064)-2


time = time[2300:3000]
four_channel_data = four_channel_data[2300:3000]

background = bg_height + bg_slope*time

def myfunct(p, fjac=None, x=None, y=None, err=None):
    # Parameter values are passed in "p"
    # If fjac==None then partial derivatives should not be
    # computed.  It will always be None if MPFIT is called with default
    # flag.
    def model_funct(time,p):
        bg_height = p[0]
        bg_slope = p[1]
        start = p[2]
        ampl = p[3]
        tau1 = p[4]
        tau2 = p[5]
        lam = np.exp(2*np.sqrt(tau1/tau2))
        return ampl*lam*np.exp(-tau1/(time-start)-(time-start)/tau2)+(bg_height + bg_slope*time)

    model = model_funct(x, p)
    # Non-negative status value means MPFIT should continue, negative means
    # stop the calculation.
    status = 0
    return([status, (y-model)/np.sqrt(model)])




from numpy import exp, linspace, random

def model(time,bg_height,bg_slope,start,ampl,tau1,tau2):
    lam = np.exp(2*np.sqrt(tau1/tau2))
    return ampl*lam*np.exp(-tau1/(time-start)-(time-start)/tau2)+(bg_height + bg_slope*time)


from scipy.optimize import curve_fit
init_vals = [1000,0.,44.,2800.,4.,2.]

best_vals, covar = curve_fit(model, time, four_channel_data, p0=init_vals)
print('best_vals: {}'.format(best_vals))