import numpy as np

sinh = np.sinh(np.pi / 2)
cosh = np.cosh(np.pi / 2)
tanh = np.tanh(np.pi / 2)
print(sinh, cosh, tanh)

sinh_arr = np.sinh(np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5]))
cosh_arr = np.cosh(np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5]))
tanh_arr = np.tanh(np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5]))
print(sinh_arr, cosh_arr, tanh_arr)

##FINDING ANGLES
print(np.arcsinh(sinh), np.arccosh(cosh), np.arctanh)
print(np.arcsinh(np.array([0.1, 0.2, 0.3])))
