import numpy as np

## ADDING TWO ARRAYS
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]

##WITHOUT UFUNC
z = []
for i, j in zip(x, y):
    z.append(i + j)
print(z)


##WITH UFUNC
z = np.add(x, y)
print(z)
