import cv2
import numpy as np
import matplotlib.pyplot as plt
I=cv2.imread('Imagine1.png',1)
I= cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
plt.plot()
plt.imshow(I,cmap = 'gray',vmin=0, vmax=255)
plt.title('Imagine Gri')
plt.axis('off')
plt.tight_layout()
plt.show()