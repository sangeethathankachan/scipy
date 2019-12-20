#Scipy optimize
import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np

def function(a):
       return   a*2 + 20 * np.sin(a)
a=np.linspace(10,20,20)
plt.plot(a, function(a))
plt.show()

optimize.fmin_bfgs(function, 0) 
#optimize.basinhopping(function, 0)
