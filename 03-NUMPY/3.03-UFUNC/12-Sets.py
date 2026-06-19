import numpy as np

arr = np.array([1, 1, 1, 1, 2, 2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5])
unique = np.unique(arr)
print(unique)

arr1 = np.array([1, 2, 3])
arr2 = np.array([3, 4, 5])
union = np.union1d(arr1, arr2)
intersection = np.intersect1d(arr1, arr2, assume_unique=True)
difference = np.setdiff1d(arr1, arr2, assume_unique=True)
symmetric_diff = np.setxor1d(arr1, arr2, assume_unique=True)

print(union, intersection, difference, symmetric_diff)
