import numpy as np

a = 4
b = 6
arr = np.arange(1, 10)

##LCM
print(np.lcm(a, b))
print(np.lcm.reduce(arr))

##GCD HCF
print(np.gcd(a, b))
print(np.gcd.reduce(arr))
