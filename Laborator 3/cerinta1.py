import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
x=np.array([3,4,-2])
y=np.array([1,1,5,4,3])
z=signal.convolve(x,y) #Convolutia semnalelor x si h n=np.arange(0,7)
n=np.arange(0,7)
#Reprezentare grafica
plt.subplot(2,2,1)
plt.stem(np.arange(0,3),x,basefmt="b") #schimbare a culorii pentru linia de baza
plt.xlim([0,7]) #definirea limitelor pentru axa Ox
plt.ylim([-3,20]) #definirea limitelor pentru axa Oy plt.xlabel('n')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.subplot(2,2,2)
plt.stem(np.arange(0,5),y,basefmt="b")
plt.xlim([0,10])
plt.ylim([0,10])
plt.xlabel('n')
plt.ylabel('y[n]')
plt.subplot(2,1,2)
plt.stem(n,z,basefmt="b")
plt.xlim([0,6])
plt.ylim([-2,40])
plt.xlabel('n')
plt.ylabel('z[n]')
plt.tight_layout()
plt.show()