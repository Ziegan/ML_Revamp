from numpy import random
import numpy as np

##SHUFFLING
S_1d_array = np.array([1,2,3,4,5])
D_1d_array = random.randint(10, size=(10))
random.shuffle(S_1d_array)
print(S_1d_array)

print(D_1d_array)
random.shuffle(D_1d_array)
print(D_1d_array)

##PERMUTATIONS
_1d_array = np.array([1,2,3,4,5])
print(random.permutation(_1d_array), _1d_array)