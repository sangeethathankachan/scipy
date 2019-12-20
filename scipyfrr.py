import numpy as np
from scipy.fftpack import fft
x=np.array([1,2,3,4,5])
y=fft(x)
print(y)
