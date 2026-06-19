import numpy as np

_1d_array_1 = np.array([1,2,3,4,5,6,7,8,9,0])
_1d_array_2 = np.array([1,2,3,4,5,5,4,3,2,1])

##SEARCH INDEX
found_1 = np.where(_1d_array_1 == 4)
found_2 = np.where(_1d_array_2 == 5)
print(found_1)
print(found_2)

##SEARCH SORTED
found_3 = np.searchsorted(_1d_array_1, 0, side='right')
found_4 = np.searchsorted(_1d_array_2, 1, side='left')
found_5 = np.searchsorted(_1d_array_1, [2,4,6])
print(found_3)
print(found_4)
print(found_5)