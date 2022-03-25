import sounddevice as sd
from scipy.io.wavfile import write
from scipy import signal
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
fs = 12000 #Frecventa de esantionare
sec = 7 # Durata inregistrarii
f=signal.firwin(32,0.8,pass_zero='lowpass')
fs,rec=read("inregistrare.wav") #Citire inregistrare
rec=rec.flatten()#redimensionarea inregistrarii intr-un vector
y=signal.convolve(rec,f)
plt.specgram(rec,Fs=fs)
plt.xlabel('Timp [s]')
plt.ylabel('Frecventa')
plt.colorbar()#Afisaza legenda culorilor
plt.show()