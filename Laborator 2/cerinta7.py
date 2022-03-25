import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
t=np.linspace(0,2,2000)
s=5*signal.square(2*np.pi*2*t,0.5)
#Definire perioade de esantionare (ms)
T1=250
#Definire semnale esantionare
u1=np.zeros((len(s)))
for i in range(1,len(s)//T1):
    u1[i*T1]=1
e1=u1*s
plt.subplot(3,1,1)
plt.plot(t,s,'--')
plt.title("$T_e$=400ms")
plt.xlabel("timp [s]")
plt.ylabel("s(t)")
plt.xticks(np.arange(0, 2.1, 0.1))
plt.plot(t,e1)
plt.tight_layout()
plt.show()