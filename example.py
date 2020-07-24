import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import sir

N=100000.0
Ns=np.array([N/3,N/3,N/3])
A = np.array([
        [1.0 ,1.0 ,1.0],
        [1.0 ,5.0 ,2.0],
        [1.0 ,4.0 ,10.0]])

rhos = np.array([0.1,0.1,0.1])
gamma = 0.5

ts=np.linspace(0,365,1000)
S0,S1,S2,I0,I1,I2,R=sir.sir(Ns,rhos,A,gamma,ts,[N/3,N/3-1,N/3,0.0,1,0.0,0.0])

plt.plot(ts,I0+I1+I2,linewidth=3)
plt.plot(ts,I0,linewidth=3)
plt.plot(ts,I1,linewidth=3)
plt.plot(ts,I2,linewidth=3)
plt.legend(["Sum","Low","Mid","High"])
plt.savefig("test.svg")


total=S0+S1+S2+I0+I1+I2+R
print("Mean: {},  std:  {}".format(np.mean(total),np.std(total)))
