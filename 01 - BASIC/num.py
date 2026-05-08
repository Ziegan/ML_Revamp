import numpy as np

#a = np.array([1,2,3,4])
#print(type(a))

#using tuple
#a = np.array((1,2,3,4))
#print(a)

#2-d array

#a = np.array([[1,2,3],[4,5,6]])
#checking dimetion
#print(a.ndim)

#checking it has 5dim

arr = np.array([1,2,3],ndmin=5)
print(arr)
print(arr.ndim)

#print(np.__version__)


