import numpy as np
import math
nn=3
pn= 6
t= np.arange(0,20,nn/100)
u = 0.1*(nn+pn)*np.cos(t-math.pi/pn)