import numpy as np
from matplotlib.pyplot import axes

arr = np.array([1, 2, 3, 4, 5, 6])
arr1 = np.array([1, 2, 3])
arr2 = np.array([3, 2, 1])

##PRODUCT CALC
print(np.prod(arr))
print(np.prod([arr1, arr2]))

##PRODUCT OVER AXIS
print(np.prod([arr1, arr2], axis=1))

##PRODUCT CUMMULATIVE
print(np.cumprod(arr))
