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

# bg_height = 1047.2220
# bg_slope = 0.025935641
# start = 44.965676
# ampl = 2823.6814
# tau1 = 4.1735936
# tau2 = 2.2154609
# taupk = 48.006471

time = (np.linspace((-nlasc), (npts-nlasc),num=npts)*0.064)-2

background = bg_height + bg_slope*time

norris_model = burst.draw_norris(time,start,ampl,tau1,tau2,background)
residuals = four_channel_data - norris_model



# def chirplet_model(time,start,ampl,tau1,tau2,background):
# def chirplet_model(x,time,I):
def chirplet_model(time, start, ampl, tau, phi, f_0, f_d):

    # lam = np.exp(2*np.sqrt(tau1/tau2))
    # inten = x[1]*lam*np.exp(-tau1/(time-x[0])-(time-x[0])/tau2)
    # inten = x[1]*np.exp(-((time-x[0])*(time-x[0]))/(x[2]*x[2]))
    # model = (inten*(np.cos((2.*np.pi*x[4]*(time-x[0]))+(np.pi*x[5]*((time-x[0])*(time-x[0])))+x[3])))
    inten = ampl*np.exp(-((time-start)*(time-start))/(tau*tau))
    model = (inten*(np.cos((2.*np.pi*f_0*(time-start))+(np.pi*f_d*((time-start)*(time-start)))+phi)))
    # for i in range(len(time)):
    #     if time[i] <= x[0]:
    #         model[i] = background[i]
    return model


# def chirp_model(x,time):
def chirp_model(time, start, ampl, tau, phi, f_0, f_d):

    # lam = np.exp(2*np.sqrt(tau1/tau2))
    # inten = x[1]*lam*np.exp(-tau1/(time-x[0])-(time-x[0])/tau2)
    # inten = x[1]*np.exp(-((time-x[0])*(time-x[0]))/(x[2]*x[2]))
    # model = (inten*(np.cos((2.*np.pi*x[4]*(time-x[0]))+(np.pi*x[5]*((time-x[0])*(time-x[0])))+x[3])))
    inten = ampl*np.exp(-((time-start)*(time-start))/(tau*tau))
    model = (inten*(np.cos((2.*np.pi*f_0*(time-start))+(np.pi*f_d*((time-start)*(time-start)))+phi)))
    # for i in range(len(time)):
    #     if time[i] <= x[0]:
    #         model[i] = background[i]
    return model


min_range = -20
max_range = 75


I_train = residuals[time>=min_range] 
time_train = time[time>=min_range] 
I_train = I_train[time_train<=max_range]
time_train = time_train[time_train<=max_range]



# x0 = np.ones(6)


# start,ampl,tau,phi,f_0,f_d
# x_0 = [50,2000,3.3,0.6,0.1,-0.1]
x_0 = [22.5260266,  3909.79703,  15.07599199, -5.32452589, 0.209558599, -0.00121162005]


# res_lsq = least_squares(chirplet_model, x_0, args=(time_train, I_train),xtol=0)
# res_lsq = least_squares(chirplet_model, x_0, args=(time_train, I_train),loss='cauchy', f_scale=0.01)
# res_lsq = minimize(chirplet_model, x_0, args=(time_train, I_train))
fitted = curve_fit(chirplet_model, time_train, I_train,p0=x_0)

print(fitted)




# plt.plot(time,four_channel_data)
# plt.plot(time,norris_model)
plt.plot(time_train,I_train)
# plt.plot(time_train,chirp_model(time_train,*x_0))
plt.plot(time_train,chirp_model(time_train,*fitted[0]))
plt.plot(time_train,chirp_model(time_train,*x_0))
plt.xlim(min_range, max_range)
plt.ylim(-5000, 6000)
# plt.ylim(-1000, 2500)
plt.legend(('Residuals',),shadow=True, loc=(0.01, 0.8), handlelength=1.5, fontsize=12)
# plt.legend(('BATSE 64ms data', 'Norris Fit'),shadow=True, loc=(0.01, 0.8), handlelength=1.5, fontsize=12)
# plt.title('00143 Residual Plot')
plt.title('BATSE Burst 00249')
plt.show()