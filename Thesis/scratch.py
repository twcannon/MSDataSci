from burst import Burst
import numpy as np
import matplotlib.pyplot as plt
import sys


# 00143: Norris Fit
out_file = '/home/thomas/git/MSDataSci/Thesis/out_files/00143_b536_3_0.out'
burst_file = './sample_data/cat64ms.00143'

burst = Burst(burst_file)
burst.parse_batse_file()

data = burst.burst_data
burst_meta = burst.header_data 
four_channel_data = np.sum(data, axis=1)

x = np.linspace((-burst_meta['nlasc']), (burst_meta['npts']-burst_meta['nlasc']),num=burst_meta['npts'])#,dtype=np.float128)
# x = np.linspace(0, burst_meta['npts'],num=burst_meta['npts'])#,dtype=np.float128)
x = x*.064
print('x',x)

bg_height = 1047.2220
bg_slope = 0.025935641
start = 44.965676/0.064
ampl = 2823.6814
tau1 = 4.1735936
tau2 = 2.2154609
taupk = 48.006471







d_t = x-start

background = bg_height + bg_slope*x

#    t_s   = p(4*ip+3)      ;  time of pulse onset with respect to timezero
#    A     = p(4*ip+4)      ;  amplitude
#    tau_1 = p(4*ip+5)      ;  rise constant
#    tau_2 = p(4*ip+6)      ;  decay constant

#    intens = A*exp(2.*sqrt(tau_1/tau_2)-tau_1/(time-t_s)-(time-t_s)/tau_2)
#    test=where(time le t_s)
#    if test(0) ne -1 then intens(test)=0.
#    intensity = intensity + intens

# intens = ampl*np.exp(2.*np.sqrt(tau1/tau2)-tau1/(d_t)-(d_t)/tau2)
# intens = ampl*np.exp(np.sqrt(tau1/tau2))#2.*np.sqrt(tau1/tau2)-tau1/(d_t)-(d_t)/tau2)
# norris_model = background + intens

lam = np.exp((2.*np.sqrt(tau1/tau2)))
print('lam',lam)

e1 = -np.exp((tau1/(x-start)))
e2 = np.exp(-(x-start)/tau2)
guts = (-(tau1/(x-start))-((x-start)/tau2)) 
print('guts',guts)
print('min(guts)',min(guts))
print('max(guts)',max(guts))
print(np.exp(guts))

print('ampl',ampl)

norris_model = (ampl*lam*guts)+background
print(norris_model)
print(min(norris_model))
print(max(norris_model))

# sys.exit()



# plt.plot(x,guts)
print(e2)
print(e1)
# plt.plot(x,e1)
# plt.plot(x,e2)
plt.plot(x,e1-e2)
# plt.plot(x,tau1/(d_t))
# plt.plot(x,-tau1/(d_t))
# plt.plot(x,-(d_t)/tau2)

# plt.plot(x,four_channel_data)
# plt.plot(x,background)
# plt.plot(x,background+(ampl*lam))
# plt.plot(x,norris_model)
plt.show()