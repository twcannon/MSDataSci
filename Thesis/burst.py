import os
import sys
import numpy as np

class Burst:

    def __init__(self,file_path):
        self.file_path = file_path


    def parse_batse_file(self):

        # open burst
        f = open(self.file_path, 'r')
        self.experiment = 'BATSE'

        # header data
        keys = f.readline().split()[:4]
        values = f.readline().split()
        self.header_data = {}
        for i in range(0,4):
            self.header_data[keys[i]] = int(values[i])

        # lightcurve data
        self.raw_data = f.read()
        self.burst_data = np.genfromtxt(self.file_path, delimiter='  ',skip_header=2)



    def summary(self,raw=False):
        if self.experiment == 'BATSE':
            print(('Header: \n{}').format(self.header_data))
        if raw:
            print(('Raw Header: \n{}{}').format(self.header_names,self.header_data))
            print(('Raw data: \n{}').format(self.raw_data))