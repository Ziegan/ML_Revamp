import numpy as np

#STATIC FILTER ARRAY
_1d_arrray = np.array([1,2,3])
filter  = [True, True, False]
filter_array = _1d_arrray[filter]
print(filter_array)

#DYNAMIC FILTER ARRAY
_1d_arrray = np.array([1,2,3,4,5,6,7,8])
filter = []

for elements in _1d_arrray:
    if elements > 5:
        filter.append(True)
    else:
        filter.append(False)
filter_array = _1d_arrray[filter]
print(filter_array)