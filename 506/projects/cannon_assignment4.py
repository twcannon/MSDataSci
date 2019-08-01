import numpy as np
from sklearn.linear_model import OrthogonalMatchingPursuit, Lasso

x=np.array([[1,8,-3,5,4,-9,4],[1,-2,4,8,-2,-3,2],[1,9,6,-7,4,-5,-5],[1,6,-14,-5,-3,9,-2],[1,-2,11,-6,3,-5,1]])
y=np.array([[-32.21],[6.10],[-37.62],[-36.60],[16.75]])

clf = Lasso(alpha=0.5)
clf.fit(x,y)

print('===========================')
print('Q1)')
print('The regularization coefficients from Lasso regression are: \n' + str(clf.coef_))

index=[]
for i in range(len(clf.coef_)):
    if clf.coef_[i] != 0:
        index.append(True)
    else:
        index.append(False)
x_l = x[:,index]
print('The new regularized X = \n' + str(x_l))

print('---------------------------')
omp = OrthogonalMatchingPursuit().fit(x_l, y)
coef = omp.coef_

print('The coefficients of the OMP sparse model are:')
for i in range(len(coef)):
    print('X{} = {}'.format(i,coef[i]))
print('===========================\n')


print('===========================')
print('Q2)')

def grad_desc(gamma):
    # dfdx (found by hand)
    dfdx = lambda x,y: 2*x-2*y-10
    # dfdy (found by hand)
    dfdy = lambda x,y: 2*y-2*x+4

    x_0 = 0
    y_0 = 2
    i = 0
    i_max = 10
    print('For gamma = {}'.format(gamma))
    print('Starting values of x and y:  \t x_0 = {}    y_0 = {}'.format(x_0,y_0))
    while i < i_max:
        x_prev = x_0
        y_prev = y_0
        x_0 = x_0 - gamma*dfdx(x_prev,y_prev)
        y_0 = y_0 - gamma*dfdy(y_prev,y_prev)

        i += 1
        if i > i_max:
            break

        # print('After iteration {}, the values of x and y are: \n'.format(i)) 
        print('For iteration = {}: \t\t x_{} = {}    y_{} = {}'.format(i,i,x_0,i,y_0))

grad_desc(0.05)
print('---------------------------')
grad_desc(0.5)
print('===========================\n')





print('===========================')
print('Q3)')
from sklearn.decomposition import PCA

data = np.genfromtxt('506/data/A.csv', delimiter = ',')

n = .70
pca = PCA(n)

pca.fit(data)
print('Using an n of {}, we are returned {} dimensions from PCA'.format(n,pca.n_components_))
print('with an explained variance of {}'.format(pca.explained_variance_))
print('and singular values of {}'.format(pca.singular_values_))
print('---------------------------')
print('===========================\n')

print(pca.__dict__)