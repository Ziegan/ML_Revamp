import numpy as np
##1D ARRAYS
##EQUAL SPLIT
_1d_array = np.array([1,2,3,4,5,6])
split = np.split(_1d_array, 2)
print(split)

##UN-EQUAL SPLIT
splitted_1d_array = np.array_split(_1d_array, 5)
print(splitted_1d_array)

##2D ARRAYS
_2d_array = np.array(([1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]))
split_1 = np.array_split(_2d_array, 3)
split_2 = np.array_split(_2d_array, 2, axis=1)
print(split_1)
print(split_2)

split_h = np.hsplit(_2d_array, 3)
split_v = np.vsplit(_2d_array, 3)
split_d = np.dsplit(_2d_array, 3)
print(split_h)
print(split_v)
print(split_d)