from scipy.special import cbrt
#Find cubic root of 27 & 64 using cbrt() function
cb = cbrt([27, 64,1000])
#print value of cb
print(cb)

#Output: array([3., 4.,10.0])

from scipy.special import exp10
#define exp10 function and pass value in its
exp = exp10([1,10])
print(exp)

#Output: [1.e+01 1.e+10] 

from scipy.special import comb
#find combinations of 5, 2 values using comb(N, k)
com = comb(5, 3, exact = False, repetition=True)
print(com)

#Output: 35.0 

from scipy.special import perm
#find permutation of 5, 2 using perm (N, k) function
per = perm(5, 2, exact = True)
print(per)

#Output: 20 
