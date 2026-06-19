from numpy import random

choosen_val = random.choice([1,2,3,4], p=[0.1, 0.6, 0.3, 0.0])
choosen_1d_arr = random.choice([1,2,3,4], p=[0.1, 0.6, 0.3, 0.0], size=(10))
choosen_2d_arr = random.choice([1,2,3,4], p=[0.1, 0.6, 0.3, 0.0], size=(5,5))
print(choosen_val)
print(choosen_1d_arr)
print(choosen_2d_arr)