import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity
# from grbpy.burst import Burst
import csv

file_path = 'tte_00138_clean.txt'

tte_list = []
with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        tte_list.append(row)
tte_array = np.asarray(tte_list)

bandwidths = [5000,15000,25000,50000]
fig, ax = plt.subplots()

line = np.linspace(int(tte_array[0][0]),
    int(tte_array[-1][0]), 1000)[:, np.newaxis]
for bandwidth in bandwidths:
    kde = KernelDensity(kernel='gaussian', bandwidth=bandwidth).fit(tte_array)
    log_dens = kde.score_samples(line)

    ax.plot(line[:, 0], np.exp(log_dens),linestyle='-',
        label="kernel bandwidth = '{0}'".format(str(bandwidth)))
ax.legend(loc='upper right')
plt.show()