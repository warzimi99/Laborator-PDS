import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
#Declarare semnale
t=np.linspace(0,1,1000) #definire timp
f2=4
v=1.5*signal.sawtooth(2*np.pi*f2*t,0.5) #semnal triunghiular
#Afisare
plt.subplot(4,1,1)
plt.plot(t,v,linewidth=2)
plt.title("Semnal triunghiular")
plt.xlabel("timp [s]")
plt.ylabel("v(t)")
plt.show()