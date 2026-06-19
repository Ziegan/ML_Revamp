import numpy as np

sample_arr = [-3.12345, 3.12345]
truncate = np.trunc(sample_arr)
print(truncate)

fix = np.fix(sample_arr)
print(fix)

rounding = np.around(sample_arr)
print(rounding)

flooring = np.floor(sample_arr)
print(flooring)

ceiling = np.ceil(sample_arr)
print(ceiling)
