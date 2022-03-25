import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
#Declarare semnale
t=np.linspace(0,1,1000) #definire timp
f3=3
r=3*signal.sawtooth(2*np.pi*f3*t) #semnal dinte de fierastrau
#Afisare
plt.subplot(4,1,1)
plt.plot(t,r,linewidth=2)
plt.title("Semnal dinte de fierastrau")
plt.xlabel("timp [s]")
plt.ylabel("r(t)")
plt.show()