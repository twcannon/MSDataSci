import math
import  matplotlib.pyplot as plt
import numpy as np

def f(t,phi):
    A   = 12.
    t_0 = 0.
    f_0 = 20.
    f_d = -1. # anti-chirping stretch  
    Q   = 5.   # width


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



def envelope(t):
    A   = 12.
    t_0 = 0.
    f_0 = 20.
    f_d = -1. # anti-chirping stretch  
    Q   = 5.   # width


    d_t = t-t_0
    tau = Q/(2.*np.pi*f_0)

    return A*np.exp(-(d_t*d_t)/(tau*tau))

x = np.linspace(-.25, .25,num=1000)
print(x)
plt.plot(x,f(x,1), label = 'asymmetric')
plt.plot(x,f(x,0), label = 'symmetric')
plt.plot(x,envelope(x), 'g:', label = 'envelope')
plt.title('Chirplets - Gaussian Envelope')
plt.legend(('asymmetric', 'symmetric', 'envelope'),shadow=True, loc=(0.01, 0.7), handlelength=1.5, fontsize=12)
plt.show()