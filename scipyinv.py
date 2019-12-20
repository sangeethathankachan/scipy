import numpy as np
from scipy.fftpack import ifft
x=np.array([1,2,3,4,5])
y=ifft(x)
print(y)
