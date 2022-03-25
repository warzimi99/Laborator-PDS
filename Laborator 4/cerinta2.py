import cv2
import numpy as np
import matplotlib.pyplot as plt
I=cv2.imread('Imagine1.png',1)
I= cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
R=I[:,:,0]
G=I[:,:,1]
B=I[:,:,2]
plt.subplot(2,2,1)
plt.hist(R.ravel(),256,[0,256])
plt.title('Histograma Rosu')
plt.subplot(2,2,2)
plt.hist(G.ravel(),256,[0,256])
plt.title('Histograma Verde')
plt.subplot(2,2,3)
plt.hist(B.ravel(),256,[0,256])
plt.title('Histograma Albastru')
plt.subplot(2,2,4)
plt.hist(I.ravel(),256,[0,256])
plt.title('Histograma totala')
plt.tight_layout()
plt.show()