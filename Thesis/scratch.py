from burst import Burst
import numpy as np
import matplotlib.pyplot as plt
import sys
import numpy.ma as ma


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
tau1 = 8.1735936
tau2 = 2.2154609
taupk = 48.006471

time = (np.linspace((-nlasc), (npts-nlasc),num=npts)*0.064)-2

background = bg_height + bg_slope*time
background = 0*time

norris_model = burst.draw_norris(time,start,ampl,tau1,tau2,background)
residuals = four_channel_data - norris_model

def chirplet_model(time,start,ampl,tau1,tau2,background):
    phi = 0.5
    f_0 = 0.28
    f_d = -0.01 # anti-chirping stretch  

    lam = np.exp(2*np.sqrt(tau1/tau2))
    inten = ampl*lam*np.exp(-tau1/(time-start)-(time-start)/tau2)
    model = inten*(np.cos((2.*np.pi*f_0*(time-start))+(np.pi*f_d*((time-start)*(time-start)))+phi))
    for i in range(len(time)):
        if time[i] <= start:
            model[i] = background[i]
    return -model

chirplet = chirplet_model(time,start,ampl,tau1,tau2,background)


# plt.plot(x,f(x,1), label = 'asymmetric')
# plt.plot(x,f(x,0), label = 'symmetric')
# plt.plot(x,envelope(x), 'g:', label = 'envelope')
# plt.show()
# plt.plot(time,four_channel_data)
plt.plot(time,norris_model, 'g:')
plt.plot(time,chirplet)
plt.xlim(30, 70)
plt.legend(('Norris Envelope', 'Chirplet'),shadow=True, loc=(0.01, 0.8), handlelength=1.5, fontsize=12)
plt.title('Example Chirplet - Norris Envelope')
# plt.plot(time,residuals)
plt.show()