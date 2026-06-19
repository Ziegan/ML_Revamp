import numpy as np


def addition(x, y):
    return x + y


myadd = np.frompyfunc(addition, 2, 1)
print(myadd([1, 2, 3], [3, 2, 1]))


##CHECKING IF A FUNCTION IS UFUNC
print(type(myadd))

if type(myadd) is np.ufunc:
    print("function is np.ufunc")
else:
    print("function is not np.ufunc")
