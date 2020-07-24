import numpy as np
from scipy.integrate import odeint

def sir(Ns,rhos,A,gamma,ts,y0):
    def fn(xs,t):
        S=xs[0:3]
        I=xs[3:6]
        R=xs[6]
        invN=1.0/Ns
        ys=np.zeros(len(xs))
        ys[0:3] = -rhos * ((A @ (invN*I)) * S)
        ys[3:6] =  rhos * ((A @ (invN*I)) * S) - gamma*I
        ys[6  ] =                                               gamma*np.sum(I)
        
        return ys
    res=odeint(fn,y0,ts)
    S0 =np.array(list(map(lambda x : x[0],res)))
    S1 =np.array(list(map(lambda x : x[1],res)))
    S2 =np.array(list(map(lambda x : x[2],res)))
    I0 =np.array(list(map(lambda x : x[3],res)))
    I1 =np.array(list(map(lambda x : x[4],res)))
    I2 =np.array(list(map(lambda x : x[5],res)))
    R  =np.array(list(map(lambda x : x[6],res)))
    return S0,S1,S2,I0,I1,I2,R
