from scipy.fft import fft
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
Fe=1000
dx=1/Fe
t=np.arange(0,2+dx,dx)
s=1.5*signal.sawtooth(2*np.pi*4*t,0.5)
F=fft(s,1024)
M=abs(F)*2*dx
f=Fe*(np.arange(0,31,1))/1024
plt.plot(f,M[0:31],color='red',linewidth='3')
plt.title("Spectrul de Amplitudini calculat cu FFT")
plt.xlabel("Frecventa [Hz]")
plt.ylabel("Amplitudinea")
plt.show()