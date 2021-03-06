from burst import Burst
import numpy as np
import matplotlib.pyplot as plt
import sys
import numpy.ma as ma
from scipy.optimize import least_squares
from scipy.optimize import minimize
from scipy.optimize import curve_fit
from scipy.signal import hilbert, chirp


pulse = '1114'

# 00143: Norris Fit
out_file = '/home/thomas/git/MSDataSci/Thesis/out_files/0'+pulse+'_b000_3_0.out'
# out_file = '/home/thomas/git/MSDataSci/Thesis/out_files/00'+pulse+'_b000_3_0.out'
# out_file = '/home/thomas/git/MSDataSci/Thesis/out_files/00'+pulse+'_b536_3_0.out'
# out_file = '/home/thomas/git/MSDataSci/Thesis/out_files/00'+pulse+'_b464_3_0.out'
burst_file = './sample_data/cat64ms.0'+pulse+''

burst = Burst(burst_file)
burst.parse_batse_file()

data       = burst.burst_data
burst_meta = burst.header_data 

four_channel_data = np.sum(data, axis=1)
trig  = burst_meta['trig#']
nlasc = burst_meta['nlasc']
npts  = burst_meta['npts']

# 1114
bg_height = 526.65551
bg_slope = -0.095278874
start = -283.41411
ampl = 430.68719
tau1 = 3989672.5
tau2 = 0.020447460
taupk = 2.2056868
min_range = -50.
max_range = 200.
y_min = -500
y_max = 1500

# # 647
# bg_height = 526.65551
# bg_slope = -0.095278874
# start = -0.60816015
# ampl = 745.10073
# tau1 = 1.0396163
# tau2 = 13.537072
# taupk = 3.1432877
# min_range = -50.
# max_range = 200.
# y_min = -500
# y_max = 1500

# # 548
# bg_height = 542.26633
# bg_slope = -0.12233601
# start = -1.4599307
# ampl = 312.91591
# tau1 = 1.9577855
# tau2 = 13.888112
# taupk = 3.7544669
# min_range = -30.
# max_range = 200.
# y_min = -200
# y_max = 1000

# bg_height = 568.34035
# bg_slope = -0.12233601
# start = -0.21628728
# ampl = 1966.6737
# tau1 = 0.37301360
# tau2 = 1.7768601
# taupk = 0.59783371
# min_range = -20.
# max_range = 20.
# y_min = -750
# y_max = 3000

# bg_height = 620.19990
# bg_slope = -0.33743619
# start = -3.7879147
# ampl = 235.19597
# tau1 = 2.2989877
# tau2 = 8.0194856
# taupk = 0.50588302
# min_range = -50.
# max_range = 100.
# y_min = -500
# y_max = 1500

# bg_height = 451.01793
# bg_slope = 0.14736013
# start = -29.530564
# ampl = 201.25052
# tau1 = 120.95145
# tau2 = 28.873298
# taupk = 29.564844
# min_range = -50.
# max_range = 200.
# y_min = -500
# y_max = 1000

# bg_height = 1047.2220
# bg_slope = 0.025935641
# start = 44.965676
# ampl = 2823.6814
# tau1 = 4.1735936
# tau2 = 2.2154609
# taupk = 48.006471
# min_range = 30.
# max_range = 70.

# bg_height = 1129.2054
# bg_slope = -0.21606104
# start = -51.924035
# ampl = 7599.8027
# tau1 = 11223.340
# tau2 = 0.48623697
# taupk = 21.948846
# min_range = -20
# max_range = 75


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


# def chirp_model(time, start, ampl, tau, phi, f_0, f_d, tau1=None, tau2=None):
#     # envelope = envelope_model(time, env_type='norris', start=start, ampl=ampl, tau1=tau1, tau2=tau2)
#     # envelope = envelope_model(time=time, env_type='bayes_wave', ampl=ampl, start=start, tau=tau)
#     # envelope = envelope_model(time=time, env_type='gauss', ampl=ampl, start=start, mean=tau1, sigma=tau2)
#     # model = envelope*(np.cos((2.*np.pi*f_0*(time-start))+(np.pi*f_d*((time-start)*(time-start)))+phi))
#     # method{‘linear’, ‘quadratic’, ‘logarithmic’, ‘hyperbolic’}, optional
#     model = envelope*(chirp(t=time, phi=phi, t1=start, f0=f_0, f1=f_d, method='linear'))
#     return model





sigma_train = np.sqrt(four_channel_data)


I_train = residuals[time>=min_range]
time_train = time[time>=min_range] 
sigma_train = sigma_train[time>=min_range]

I_train = I_train[time_train<=max_range]
sigma_train = sigma_train[time_train<=max_range]
time_train = time_train[time_train<=max_range]



env_x_0 = [start,ampl,tau1,tau2]

def norris_envelope_model(time, start=None, ampl=None, tau1=None, tau2=None):
    lam = np.exp(2.*np.sqrt(tau1/tau2))
    model = ampl*lam*np.exp(-tau1/(time-start)-(time-start)/tau2)
    background = 0*time
    for i in range(len(time)):
        if time[i] <= start:
            model[i] = background[i]
    return model

def bayes_wave_envelope_model(time, start=None, ampl=None, tau=None):
    model = ampl*np.exp(-((time-start)*(time-start))/(tau*tau))
    return model


# bayes_env = curve_fit(f=bayes_wave_envelope_model, xdata=time_train, ydata=amplitude_envelope, p0=[start,ampl,tau2], maxfev=10000, check_finite=True)
# envelope = norris_envelope_model(time_train, *env_x_0)
# envelope = bayes_wave_envelope_model(time_train, *bayes_env[0])

analytic_signal = hilbert(I_train)
amplitude_envelope = np.abs(analytic_signal)

def chirp_model(time, start, ampl, tau, phi, f_0, f_d, tau1=None, tau2=None, env_ampl=None, env_start=None):
    lam = np.exp(2.*np.sqrt(tau1/tau2))
    # envelope = env_ampl*lam*np.exp(-tau1/(time-env_start)-(time-env_start)/tau2)
    envelope = env_ampl*lam*np.exp(-tau1/(time-start)-(time-start)/tau2)
    background = 0*time
    for i in range(len(time)):
        # if time[i] <= env_start:
        if time[i] <= start:
            envelope[i] = background[i]
    model = envelope*(ampl*chirp(t=time, phi=phi, t1=start, f0=f_0, f1=f_d, method='linear'))
    # model = envelope*(np.cos((2.*np.pi*f_0*(time-start))+(np.pi*f_d*((time-start)*(time-start)))+phi))
    return model

# envelope = envelope_model(time, env_type='norris', start=start, ampl=ampl, tau1=tau1, tau2=tau2)
# envelope = envelope_model(time=time, env_type='bayes_wave', ampl=ampl, start=start, tau=tau)
# envelope = envelope_model(time=time, env_type='gauss', ampl=ampl, start=start, mean=tau1, sigma=tau2)



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
x_0 = [start,  ampl/100,  0, 0.05, -0.00001,  0.01,  tau1,  tau2, ampl/2, start-2]



fitted = curve_fit(f=chirp_model, xdata=time_train, ydata=I_train, p0=x_0, maxfev=1000000, check_finite=True, sigma=sigma_train)
# fitted = curve_fit(f=chirp_model, xdata=time_train, ydata=I_train, p0=x_0, maxfev=10000, check_finite=True, bounds=(min_range, max_range))
# fitted = curve_fit(f=chirp_model, xdata=time_train, ydata=I_train, p0=x_0, maxfev=5000, sigma=sigma, check_finite=True)

# print(fitted)


plt.plot(time,four_channel_data,  label='4-channel')
# plt.plot(time,norris_model)
# plt.plot(time_train,I_train)

plt.plot(time_train, norris_envelope_model(time_train,*[start,ampl,tau1,tau2])+(bg_slope*time_train)+bg_height, label='norris')
plt.plot(time_train,I_train,  label='residuals')
plt.plot(time_train,chirp_model(time_train,*fitted[0]), label='chirplet')
plt.plot(time_train, norris_envelope_model(time_train,*[start,ampl,tau1,tau2])+(bg_slope*time_train)+chirp_model(time_train,*fitted[0])+bg_height, 'k', label='chirplet + norris')
# plt.plot(time_train,amplitude_envelope)
# plt.plot(time_train,chirp_model(time_train,*x_0))
# plt.plot(time_train,norris_envelope_model(time_train,*env_x_0))
# plt.plot(time_train,norris_envelope_model(time_train,*norris_env[0]))
# plt.plot(time_train,bayes_wave_envelope_model(time_train, *bayes_env[0]))
# plt.plot(time_train,chirp_model(time_train,*x_0))


# plt.plot(time_train,burst.draw_norris(time_train,fitted[0][0],fitted[0][1],fitted[0][6],fitted[0][7],np.zeros(len(time_train))))
plt.xlim(min_range, max_range)
plt.ylim(y_min, y_max)
# plt.ylim(-1000, 2500)
# plt.legend(('Residuals',),shadow=True, loc=(0.01, 0.8), handlelength=1.5, fontsize=12)
# plt.legend(('BATSE 64ms data', 'Norris Fit'),shadow=True, loc=(0.01, 0.8), handlelength=1.5, fontsize=12)
# plt.title('00143 Residual Plot')
plt.legend()
plt.title('BATSE Burst 00'+pulse)
plt.show()