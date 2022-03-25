import numpy as np
nn=3
pn= 6
A = np.array ([[1, 2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]]) 
B = np.ones( ( pn, pn ) )
C = np.matmul ( A, B )
print (C)