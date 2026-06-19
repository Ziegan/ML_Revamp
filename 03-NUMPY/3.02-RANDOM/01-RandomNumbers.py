import numpy as np

##PSUDO RANDOM
rand_int = np.random.randint(100)
rand_float = np.random.rand()
rand_array_1d = np.random.randint(100, size=(5))
rand_array_2d = np.random.randint(100, size=(5,2))
rand_array_3d = np.random.randint(100, size=(5,5,5))
print(rand_int, rand_float)
print(rand_array_1d)
print(rand_array_2d)
print(rand_array_3d)

##CHOICE BASED RANDOM
chosen = np.random.choice([1,2,3,4,5,6], size=(3,2))
print(chosen)