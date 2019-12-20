from scipy import special
from scipy import integrate

i=integrate.quad(lambda x:special.exp10(x),0,1)
print(i)
