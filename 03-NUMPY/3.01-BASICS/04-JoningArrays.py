import numpy as np

##CONCATENATE
##1D
_1d_array_1 = np.array([1,2,3])
_1d_array_2 = np.array((4,5,6))

print(_1d_array_1, _1d_array_2)

_1d_array_3 = np.concatenate((_1d_array_1, _1d_array_2))
print(_1d_array_3)

##2D
_2d_array_1 = np.array([[1,2,3], [4,5,6]])
_2d_array_2 = np.array([(0,9,8), (7,6,5)])
_2d_array_3 = np.concatenate((_2d_array_1, _2d_array_2))
_2d_array_4 = np.concatenate((_2d_array_1, _2d_array_2), axis=1)
print(_2d_array_3)
print(_2d_array_4)

##STACK
_1d_array_stack_1 = np.stack((_1d_array_1, _1d_array_2))
_1d_array_stack_2 = np.stack((_1d_array_1, _1d_array_2), axis=1)
print(_1d_array_stack_1)
print(_1d_array_stack_2)

_1d_array_hstack = np.hstack((_1d_array_1, _1d_array_2))
_1d_array_vstack = np.vstack((_1d_array_1, _1d_array_2))
_1d_array_dstack = np.dstack((_1d_array_1, _1d_array_2))
print(_1d_array_hstack)
print(_1d_array_vstack)
print(_1d_array_dstack)