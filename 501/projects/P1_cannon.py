import numpy as np
import matplotlib.pyplot as plt

sample_data = np.genfromtxt('501/data/project_one/TABLE2.csv', delimiter = ',')

print(sample_data)

T,S,D = np.linalg.svd(sample_data, full_matrices = False)

# print(S)
Si = 1/S
Si = Si*np.identity(9)
print('---------T----------')
print(T)
print('---------D----------')
print(D)
Dt = np.transpose(D)
print('---------Dt----------')
print(Dt)


X = [[0,0,0,1,0],
    [1,0,1,0,0],
    [1,1,0,0,0],
    [1,1,1,0,1],
    [0,0,1,2,0],
    [0,1,0,1,1],
    [0,1,0,0,0],
    [0,0,1,1,0],
    [0,1,1,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]]


print('---------Si----------')
print(Si)
print('---------T----------')
print(T)
print('----------')

Q = np.matmul(np.matmul(np.transpose(X),T),Si)

print('---------Q----------')
print(Q)

print(type(T))
print(type(Q))

plt.scatter(T[:,0],  T[:,1],  color='red',   marker='.', label='Terms')
plt.scatter(Dt[:,0], Dt[:,1], color='blue',  marker='s', label='Documents')
plt.scatter(Q[:,0],  Q[:,1],  color='green', marker='x', label='Queries')

plt.legend()
plt.show()