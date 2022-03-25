import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
#Declarare semnale
t=np.linspace(0,1,1000) #definire timp
f1=2
p=5*signal.square(2*np.pi*f1*t,0.5) #semnal dreptunghiular
#Afisare
plt.subplot(4,1,1)
plt.plot(t,p,linewidth=2)
plt.title("Semnal dreptunghiular")
plt.xlabel("timp [s]")
plt.ylabel("p(t)")
plt.show()