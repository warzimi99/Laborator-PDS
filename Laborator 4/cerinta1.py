import cv2
import matplotlib.pyplot as plt
I=cv2.imread('Imaginea1.jpeg',1)
I=cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
R=I[:,:,0] #Salveaza componenta 0 pentru fiecare element din matrice
G=I[:,:,1] #Salveaza componenta 1 pentru fiecare element din matrice
B=I[:,:,2] #Salveaza componenta 2 pentru fiecare element din matrice
plt.figure(0)
plt.subplot(2,2,1)
plt.imshow(R, cmap='gray', vmin=0, vmax=255)
plt.title('Canal R')
plt.axis('off')
plt.subplot(2,2,2)
plt.imshow(G, cmap='gray', vmin=0, vmax=255)
plt.title('Canal G')
plt.axis('off')
plt.subplot(2,2,3)
plt.imshow(B, cmap='gray', vmin=0, vmax=255)
plt.title('Canal B')
plt.axis('off')
plt.subplot(2,2,4)
plt.imshow(I)
plt.title('Imagine color')
plt.axis('off')
plt.tight_layout()
plt.show()