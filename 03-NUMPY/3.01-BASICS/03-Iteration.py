import numpy as np

_1D_arr = np.array([1,2,3,4,5])
_2D_arr = np.array([[1, 2, 3], [4, 5, 6]])

for elements in _1D_arr:
    print(elements)

for inner_arr in _2D_arr:
    print(inner_arr)
    for elements in inner_arr:
        print(elements)

for elements in np.nditer(_2D_arr):
    print("Values From 2D array >", elements)

for skipped_elements in np.nditer(_2D_arr[:, ::2]):
    print(skipped_elements)

print(_2D_arr)
print(np.flip(_2D_arr))