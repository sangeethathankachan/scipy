from scipy.stats import norm,uniform
import numpy as np

print norm.cdf(np.array([1,-1., 0, 1, 3, 4, -2, 6]))
print uniform.cdf([0, 1, 2, 3, 4, 5], loc = 1, scale = 4)
