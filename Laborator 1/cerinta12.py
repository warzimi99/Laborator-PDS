import numpy as np
import math
import matplotlib.pyplot as plt
nn=3
pn= 6
t= np.arange(0,20,nn/100)
s = np.sin(t+math.pi/nn)
plt.plot(t,s)
plt.show()