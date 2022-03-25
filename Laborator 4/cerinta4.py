import cv2
import numpy as np
import matplotlib.pyplot as plt
I=cv2.imread('Imagine1.png',1)
I= cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
G3 = 1/16*np.array([[1, 2, 1],[2, 4, 2],[1, 2, 1]])#nucleu gaussian 3x3
F = np.zeros((I.shape))
F = cv2.filter2D(src=I, ddepth=-1, kernel=G3)
plt.imshow(F.astype('uint8'))
plt.axis('off')
plt.show()