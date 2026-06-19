import numpy as np

##NORMAL ADDITION
arr1 = np.array([1, 2, 3])
arr2 = np.array([3, 2, 1])
print(np.add(arr1, arr2))

##SUMMING
print(np.sum([arr1, arr2]))

##SUMMING OVER AXIS
print(np.sum([arr1, arr2], axis=1))

##CUMMULATIVE SUM
print(np.cumsum(arr1))
