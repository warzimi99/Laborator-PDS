import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
f=signal.firwin(32,0.6,pass_zero='lowpass')
#Afisare
w,h=signal.freqz(f) #Generare componente amplitudine si faza pentru FIR anterior
w=w/np.pi
plt.subplot(2,1,1)
plt.plot(w,20*np.log10(abs(h)),'b')
plt.xlabel('Frecventa normata [x$\pi$ rad/esantion]')
plt.ylabel('Amplitudine [dB]')
plt.xlim([0,1])
plt.grid()
plt.subplot(2,1,2)
angles=np.unwrap(np.angle(h))
plt.plot(w,angles,'g')
plt.xlabel('Frecventa normata [x$\pi$ rad/esantion]')
plt.ylabel('Faza [grade]')
plt.xlim([0,1])
plt.grid()
plt.tight_layout()
plt.show()