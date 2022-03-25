import sounddevice as sd
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
fs = 12000 
#Frecventa de esantionare
sec = 7 
# Durata inregistrarii
#Inregistrare audio
rec = sd.rec(int(sec * fs), samplerate=fs, channels=1)
sd.wait()
rec=rec.flatten() 
#redimensionarea inregistrarii intr-un vector
write('inregistrare.wav', fs, rec) 
#salvare inregistrare
plt.specgram(rec,Fs=fs)
plt.xlabel('Timp [s]')
plt.ylabel('Frecventa')
plt.colorbar
()#Afisaza legenda culorilor
plt.show()
#am in folder si mostre audio daca nu merge sa inregistrez cu microfonul!