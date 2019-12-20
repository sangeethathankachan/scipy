#Linear Algebra with Scipy
from scipy import linalg
import numpy as np
#define square matrix
two_d_array = np.array([ [4,5], [3,2] ])
#pass values to det() function
print(linalg.det( two_d_array ))

#Output: -7.0 

#Inverse
#pass value to function inv()
print(linalg.inv( two_d_array ))
eg_val,eg_vec=linalg.eig(two_d_array)
print(eg_val)
print(eg_vec)
'''Output:

array( [[-0.28571429,  0.71428571],
       [ 0.42857143, -0.57142857]] )'''

from scipy import linalg
import numpy as np
#define two dimensional array
arr = np.array([[5,4],[6,3]])
#pass value into function
eg_val, eg_vect = linalg.eig(arr)
#get eigenvalues
print(eg_val)
#get eigenvectors
print(eg_vect)

'''Output:

[ 9.+0.j -1.+0.j] #eigenvalues
 [ [ 0.70710678 -0.5547002 ] #eigenvectors
   [ 0.70710678  0.83205029] ]'''




