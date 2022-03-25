import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
#Declarare semnale
t=np.linspace(0,1,1000) #definire timp
f1=2
f2=4
f3=3
p=5*signal.square(2*np.pi*f1*t,0.5)
v=1.5*signal.sawtooth(2*np.pi*f2*t,0.5)
s=3*signal.sawtooth(2*np.pi*f3*t)
#Afisare
plt.subplot(4,1,1)
plt.plot(t,p,linewidth=2)
plt.title("Semnal dreptunghiular")
plt.xlabel("timp [s]")
plt.ylabel("p(t)")
plt.subplot(4,1,2)
plt.plot(t,v,linewidth=2)
plt.title("Semnal triunghiular")
plt.xlabel("timp [s]")
plt.ylabel("v(t)")
plt.tight_layout()
plt.subplot(4,1,3)
plt.plot(t,s,linewidth=2)
plt.title("Semnal dinte de fierastrau")
plt.xlabel("timp [s]")
plt.ylabel("s(t)")
plt.tight_layout()
plt.show()