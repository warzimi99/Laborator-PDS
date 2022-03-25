import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
dt=0.001
t=np.arange(0+dt,2+dt,dt)
s=5*signal.square(2*np.pi*2*t,0.5) #semnal dreptunghiular cerinta 5
#Reprezentarea in timp a semnalului
plt.subplot(1,2,1)
plt.plot(t,s,linewidth=2)
plt.title("Semnalul periodic")
plt.xlabel("timp [s]")
plt.ylabel("s(t)")
#Definire vectori Fourier
n=30 #Numarul de frecvente analizate
A=np.zeros((n))
B=np.zeros((n))
M=np.zeros((n))
P=np.zeros((n))
#Calcularea coeficientilor Fourier
for i in range(1,n):
    A[i]=sum(s*np.cos(2*np.pi*i*t))*dt
    B[i]=sum(s*np.sin(2*np.pi*i*t))*dt
    M[i]=np.sqrt(np.power(A[i],2)+np.power(B[i],2))
    P[i]=-np.arctan(B[i]/A[i])
#Reprezentarea spectrelor
plt.subplot(2,2,2)
plt.stem(M)
plt.title("Spectru amplitudini")
plt.xlabel("Frecventa [Hz]")
plt.ylabel("Amplitudine [V]")
plt.subplot(2,2,4)
plt.stem(P)
plt.title("Spectru faze")
plt.xlabel("Frecventa [Hz]")
plt.ylabel("Faza [rad]")
plt.tight_layout()
plt.show()