import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt

debug = True



dtype = [('burst','S50'),
            ('class','S50'),
            ('3 class','S50'),
            ('complete','S50'),
            ('duration','f8'),
            ('sig_dur','f8'),
            ('sig_asym','f8'),
            ('sig_lag','f8'),
            ('pulse pk flux','f8'),
            ('sig_pk flux','f8'),
            ('S(1+2+3)','f8'),
            ('sigS(1+2+3)','f8'),
            ('hr31 (erg)','f8'),
            ('sig hr31 (erg)','f8'),
            ('log10(dur)','f8'),
            ('asymmetry','f8'),
            ('lag','f8'),
            ('log10(p256)','f8'),
            ('log10(S)','f8'),
            ('log10(hr31)','f8')]

data = np.genfromtxt('501/data/project_two/2010 GRB pulse table.csv', delimiter = ',', names=True, dtype=dtype)
print('Data: \n'+str(data)) if debug else next