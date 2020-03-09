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

background = bg_height + bg_slope*time

norris_model = burst.draw_norris(time,start,ampl,tau1,tau2,background)
residuals = four_channel_data - norris_model

plt.plot(time,four_channel_data)
plt.plot(time,norris_model)
plt.plot(time,residuals)
plt.show()