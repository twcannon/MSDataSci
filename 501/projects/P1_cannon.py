import numpy as np
import matplotlib.pyplot as plt

sample_data = np.genfromtxt('501/data/project_one/TABLE2.csv', delimiter = ',')

print(sample_data)

T,S,D = np.linalg.svd(sample_data, full_matrices = False)

# print(T)
print(S*np.identity(9))
# print(D)

X = [[0,0,1,1,2],
    [0,0,0,0,0],
    [1,0,0,2,0],
    [0,0,0,1,1],
    [0,0,0,0,1],
    [1,1,0,0,0],
    [1,0,0,0,1],
    [1,2,0,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [1,1,1,1,1],
    [0,1,0,1,0]]

Xt = np.transpose(X)

print(Xt)