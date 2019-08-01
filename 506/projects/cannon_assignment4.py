import numpy as np
from sklearn.linear_model import OrthogonalMatchingPursuit, Lasso

x=np.array([[1,8,-3,5,4,-9,4],[1,-2,4,8,-2,-3,2],[1,9,6,-7,4,-5,-5],[1,6,-14,-5,-3,9,-2],[1,-2,11,-6,3,-5,1]])
y=np.array([[-32.21],[6.10],[-37.62],[-36.60],[16.75]])

print(x)
print(y)

clf = Lasso(alpha=0.5)
clf.fit(x,y)
print(clf.coef_)
print(clf.intercept_)


# reg = OrthogonalMatchingPursuit().fit(x, y)

# reg.set_params(s=0.5)



cur_x = 3 # The algorithm starts at x=3
rate = 0.01 # Learning rate
precision = 0.000001 #This tells us when to stop the algorithm
previous_step_size = 1 #
max_iters = 10000 # maximum number of iterations
iters = 0 #iteration counter
df = lambda x: 2*(x+5) #Gradient of our function
In [4]:
while previous_step_size > precision and iters < max_iters:
    prev_x = cur_x #Store current x value in prev_x
    cur_x = cur_x - rate * df(prev_x) #Grad descent
    previous_step_size = abs(cur_x - prev_x) #Change in x
    iters = iters+1 #iteration count
    print("Iteration",iters,"\nX value is",cur_x) #Print iterations
    
print("The local minimum occurs at", cur_x)





# dfdx (found by hand)
dfdx = lambda x,y: 2*x-2*y-10

# dfdy (found by hand)
dfdy = lambda x,y: 2*y-2*x+4


x_0 = 0
y_0 = 2
gamma = .01
i_max = 10

i = 0
print('Starting values of x and y: \n x_0 = {}    y_0 = {}\n'.format(x,y))
while i < i_max:
    x_prev = x_0
    y_prev = y_0
    x_new = x_0 - gamma*N(dfdx.subs(x,x_0).subs(y,y_0)).evalf()
    y_new = y_0 - gamma*N(dfdy.subs(y,y_0)).subs(x,x_0).evalf()

    i += 1
    if i > i_max:
        break

    x_0 = x_new
    y_0 = y_new

    print('After iteration {}, the values of x and y are: \n') 
    print('\t for gamma = {}: \t\t x_{} = {}    y_{} = {}\n'.format(gamma,i,i,x,i,y))