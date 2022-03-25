import cv2
import numpy as np
import matplotlib.pyplot as plt
I=cv2.imread('Imagine1.png',1)
I= cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
SH = np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]])
F = np.zeros((I.shape))
F = cv2.filter2D(src=I, ddepth=-1, kernel=SH)
plt.imshow(F.astype('uint8'))
plt.axis('off')
plt.show()