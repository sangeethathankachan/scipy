from scipy import integrate
# take f(x) function as f
f = lambda x : x**2
#single integration with a = 0 & b = 1  
integration = integrate.quad(f, 0 , 1)
print(integration)

'''Output:

(0.33333333333333337, 3.700743415417189e-15)'''

