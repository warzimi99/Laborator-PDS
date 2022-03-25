import numpy as np
from scipy import linalg
nn=3
pn= 6
D =np.array([[nn,pn-20,nn*0.42], [nn+pn, pn*2,1], [nn-pn,nn/pn,3]])
d = linalg.det(D)
print(d)