from burst import Burst
import numpy as np
import matplotlib.pyplot as plt
import sys
import numpy.ma as ma


# 00143: Norris Fit
out_file = '/home/thomas/git/MSDataSci/Thesis/out_files/00143_b536_3_0.out'
# out_file = '/home/thomas/git/MSDataSci/Thesis/out_files/00249_b464_3_0.out'
# burst_file = './sample_data/cat64ms.00249'
burst_file = './sample_data/cat64ms.00143'

burst = Burst(burst_file)
burst.parse_batse_file()

data       = burst.burst_data
burst_meta = burst.header_data 

four_channel_data = np.sum(data, axis=1)
trig  = burst_meta['trig#']
nlasc = burst_meta['nlasc']
npts  = burst_meta['npts']

# bg_height = 1129.2054
# bg_slope = -0.21606104
# start = -51.924035
# ampl = 7599.8027
# tau1 = 11223.340
# tau2 = 0.48623697
# taupk = 21.948846

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

# plt.plot(time,four_channel_data)
# plt.plot(time,norris_model)
plt.plot(time,residuals)
# plt.xlim(-20, 80)
plt.xlim(30, 70)
# plt.ylim(500, 7000)
plt.ylim(-1000, 2500)
plt.legend(('Residuals',),shadow=True, loc=(0.01, 0.8), handlelength=1.5, fontsize=12)
# plt.legend(('BATSE 64ms data', 'Norris Fit'),shadow=True, loc=(0.01, 0.8), handlelength=1.5, fontsize=12)
# plt.title('00143 Residual Plot')
plt.title('BATSE Burst 00143')
plt.show()