import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt

debug = False




sample_data = np.genfromtxt('501/data/project_one/TABLE2.csv', delimiter = ',')
print('Sample Data: \n'+sample_data) if debug else next

doc_labels = ['cl','c2','c3','c4','c5','m1','m2','m3','m4']
terms = ['human','interface','computer','user','system','response','time','EPS','survey','trees','graph','minors']





T,S,D = np.linalg.svd(sample_data, full_matrices = False)
print('Calculated T Data: \n'+T) if debug else next
print('Calculated S Data: \n'+S) if debug else next
print('Calculated D Data: \n'+D) if debug else next

Si = 1/S
Si = Si*np.identity(9)
print('S Inverse: \n'+Si) if debug else next

Dt = np.transpose(D)
print('Transposed D: \n'+Dt) if debug else next







def plot_labels(data,labels,offset):
    for i in range(len(labels)):
        plt.text(data[i,0]+offset, data[i,1]-offset, labels[i], fontsize=8)







plt.scatter(T[:,0],  T[:,1],  color='red',   marker='.', label='Terms')
plt.scatter(Dt[:,0], Dt[:,1], color='blue',  marker='s', label='Documents')
plot_labels(T,terms,0.015)
plot_labels(Dt,doc_labels,0.015)
plt.title('2-D plot of Terms and Documents with Queries')
plt.xlabel('Dimension-1')
plt.ylabel('Dimension-2')
plt.legend()
plt.show()







q_labels = ['q1','q2','q3','q4','q5']
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

Q = np.matmul(np.matmul(np.transpose(X),T),Si)
print('Calculated Query Data: \n'+Q) if debug else next








plt.scatter(T[:,0],  T[:,1],  color='red',   marker='.', label='Terms')
plt.scatter(Dt[:,0], Dt[:,1], color='blue',  marker='s', label='Documents')
plt.scatter(Q[:,0],  Q[:,1],  color='green', marker='x', label='Queries')
plot_labels(T,terms,0.015)
plot_labels(Dt,doc_labels,0.015)
plot_labels(Q,q_labels,0.015)
plt.title('2-D plot of Terms and Documents with Queries')
plt.xlabel('Dimension-1')
plt.ylabel('Dimension-2')
plt.legend()
plt.show()









T_dist_list = []
T_dist_index = []
Dt_dist_list = []
Dt_dist_index = []
for i in range(len(Q)):
    T_dist_list.append([np.inf,np.inf,np.inf])
    T_dist_index.append([np.inf,np.inf,np.inf])
    Dt_dist_list.append([np.inf,np.inf,np.inf])
    Dt_dist_index.append([np.inf,np.inf,np.inf])
    q=Q[i,0:2]

    for j in range(len(T)):
        t=T[j,0:2]
        list_max = np.amax(T_dist_list[i])
        min_index = np.where(T_dist_list[i] == np.amax(list_max))[0][0]
        d = spatial.distance.cosine(q, t)
        if d < list_max:
            T_dist_list[i][min_index] = d
            T_dist_index[i][min_index] = j
        print(T_dist_list) if debug else next
        print(T_dist_index) if debug else next

    for k in range(len(Dt)):
        dt=Dt[k,0:2]
        list_max = np.amax(Dt_dist_list[i])
        min_index = np.where(Dt_dist_list[i] == np.amax(list_max))[0][0]
        d = spatial.distance.cosine(q, t)
        if d < list_max:
            Dt_dist_list[i][min_index] = d
            Dt_dist_index[i][min_index] = k
        print(Dt_dist_list) if debug else next
        print(Dt_dist_index) if debug else next







for i in range(len(Q)):
    print('\nThe three closest Terms by cosine distance to Query {} are:'.format(q_labels[i]))
    for j in range(len(T_dist_list[i])):
        print('    Term: {}, by a distance of: {}'.format(terms[T_dist_index[i][j]],T_dist_list[i][j]))

for i in range(len(Q)):
    print('\nThe three closest Documents by cosine distance to Query {} are:'.format(q_labels[i]))
    for j in range(len(T_dist_list[i])):
        print('    Document: {}, by a distance of: {}'.format(doc_labels[T_dist_index[i][j]],T_dist_list[i][j]))





