from burst import Burst
import numpy as np
import matplotlib.pyplot as plt
import sys
import numpy.ma as ma
from scipy.optimize import least_squares
from scipy.optimize import minimize
from scipy.optimize import curve_fit


# 00143: Norris Fit
# out_file = '/home/thomas/git/MSDataSci/Thesis/out_files/00143_b536_3_0.out'
out_file = '/home/thomas/git/MSDataSci/Thesis/out_files/00249_b464_3_0.out'
# burst_file = './sample_data/cat64ms.00143'
burst_file = './sample_data/cat64ms.00249'

burst = Burst(burst_file)
burst.parse_batse_file()

data       = burst.burst_data
burst_meta = burst.header_data 

four_channel_data = np.sum(data, axis=1)
trig  = burst_meta['trig#']
nlasc = burst_meta['nlasc']
npts  = burst_meta['npts']

bg_height = 1129.2054
bg_slope = -0.21606104
start = -51.924035
ampl = 7599.8027
tau1 = 11223.340
tau2 = 0.48623697
taupk = 21.948846
min_range = -20
max_range = 75


# bg_height = 1047.2220
# bg_slope = 0.025935641
# start = 44.965676
# ampl = 2823.6814
# tau1 = 4.1735936
# tau2 = 2.2154609
# taupk = 48.006471
# min_range = 30.
# max_range = 70.


time = (np.linspace((-nlasc), (npts-nlasc),num=npts)*0.064)-2

background = bg_height + bg_slope*time

norris_model = burst.draw_norris(time,start,ampl,tau1,tau2,background)
residuals = four_channel_data - norris_model



def envelope_model(time, env_type, start=None, ampl=None, tau=None, tau1=None, tau2=None, mean=None, sigma=None):
    if env_type == 'norris':
        lam = np.exp(2*np.sqrt(tau1/tau2))
        return ampl*lam*np.exp(-tau1/(time-start)-(time-start)/tau2)
    elif env_type == 'bayes_wave':
        return ampl*np.exp(-((time-start)*(time-start))/(tau*tau))
    elif env_type == 'gauss':
        return ampl*np.exp(-(time-mean)**2/(2*sigma**2))
    else:
       return None


def chirp_model(time, start, ampl, tau, phi, f_0, f_d, tau1=None, tau2=None):
    envelope = envelope_model(time, env_type='norris', start=start, ampl=ampl, tau1=tau1, tau2=tau2)
    # envelope = envelope_model(time=time, env_type='bayes_wave', ampl=ampl, start=start, tau=tau)
    # envelope = envelope_model(time=time, env_type='gauss', ampl=ampl, start=start, mean=tau1, sigma=tau2)
    model = envelope*(np.cos((2.*np.pi*f_0*(time-start))+(np.pi*f_d*((time-start)*(time-start)))+phi))
    return model







I_train = residuals[time>=min_range] 
time_train = time[time>=min_range] 
I_train = I_train[time_train<=max_range]
time_train = time_train[time_train<=max_range]

# sigma = np.sqrt(I_train)

# I_train = abs(I_train)
# print(I_train) 


# x0 = np.ones(6)


# start,ampl,tau,phi,f_0,f_d,tau1,tau2
# x_0 = [50,2000,3.3,0.6,0.1,-0.1]
# x_0 = [20.,  4000.,  3., -5., 0.2, -0.01, 1000, 200]
# x_0 = [2.25260155e+01,  3.90974125e+03,  3.07607879e+00, -5.32453311e+00, 2.09559818e-01, -1.21171999e-02]
# x_0 = [20.,  4000.,  3., -5., 0.2, -0.01]
# x_0 = [min_range,  ampl,  10, -5., 1.,  1.,  tau1,  tau2]
# start,ampl,tau,phi,f_0,f_d,tau1,tau2
x_0 = [start-2,  ampl,  0, 0, 0.01,  0.001,  tau1*1.1,  tau2]



fitted = curve_fit(f=chirp_model, xdata=time_train, ydata=I_train, p0=x_0, maxfev=10000, check_finite=True)
# fitted = curve_fit(f=chirp_model, xdata=time_train, ydata=I_train, p0=x_0, maxfev=10000, check_finite=True, bounds=(min_range, max_range))
# fitted = curve_fit(f=chirp_model, xdata=time_train, ydata=I_train, p0=x_0, maxfev=5000, sigma=sigma, check_finite=True)

print(fitted)


# plt.plot(time,four_channel_data)
# plt.plot(time,norris_model)
plt.plot(time_train,I_train)
# plt.plot(time_train,chirp_model(time_train,*x_0))
plt.plot(time_train,chirp_model(time_train,*x_0))
plt.plot(time_train,chirp_model(time_train,*fitted[0]))
# plt.plot(time_train,chirp_model(time_train,*x_0))
# plt.plot(time_train,burst.draw_norris(time_train,fitted[0][0],fitted[0][1],fitted[0][6],fitted[0][7],np.zeros(len(time_train))))
plt.xlim(min_range, max_range)
plt.ylim(-5000, 6000)
# plt.ylim(-1000, 2500)
plt.legend(('Residuals',),shadow=True, loc=(0.01, 0.8), handlelength=1.5, fontsize=12)
# plt.legend(('BATSE 64ms data', 'Norris Fit'),shadow=True, loc=(0.01, 0.8), handlelength=1.5, fontsize=12)
# plt.title('00143 Residual Plot')
plt.title('BATSE Burst 00249')
plt.show()