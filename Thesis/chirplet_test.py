import math
import  matplotlib.pyplot as plt
import numpy as np

def f(t):
    A   = 12.
    t_0 = 0.
    f_0 = 20.
    f_d = -1. # anti-chirping stretch  
    Q   = 5.   # width
    phi = 1.   # offset

    d_t = t-t_0
    tau = Q/(2.*np.pi*f_0)

    # print(d_t)
    # print(tau)
    # print(np.pi)

    print('exp')
    d_t_0 = t[0]-t_0
    print(d_t_0)
    print((d_t_0*d_t_0))
    print(-(d_t_0*d_t_0))
    print((tau*tau))
    print(-(d_t_0*d_t_0)/(tau*tau))
    print(np.exp(-(d_t_0*d_t_0)/(tau*tau)))
    print('cos')
    print((2.*np.pi*f_0*d_t_0))
    print((np.pi*f_d*(d_t_0*d_t_0)))
    print(phi)
    print((2.*np.pi*f_0*d_t_0)+(np.pi*f_d*(d_t_0*d_t_0))+phi)
    print(np.cos((2.*np.pi*f_0*d_t_0)+(np.pi*f_d*(d_t_0*d_t_0))+phi))

    return A*np.exp(-(d_t*d_t)/(tau*tau))*np.cos((2.*np.pi*f_0*d_t)+(np.pi*f_d*(d_t*d_t))+phi)


x = np.linspace(-.25, .25,num=1000)
print(x)
print(f(x))
plt.plot(x,f(x), label = 'f(x)')
plt.show()