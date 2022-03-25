import numpy as np
import math
import matplotlib.pyplot as plt
nn=3
pn= 6
t= np.arange(0,20,nn/100)
s = np.sin(t+math.pi/nn)
u = 0.1*(nn+pn)*np.cos(t-math.pi/pn)
plt.plot(t,s)
plt.plot(t,u)
plt.title("Reprezentare grafică funcția s(t) și u(t)")
plt.xlabel("Timp(s)")
plt.ylabel("s(t),u(t)")
plt.legend(["s(t)","u(t)"],fontsize=14,loc="center left")
plt.show()