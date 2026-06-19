import numpy as np

arr_by_list = np.array([1,2,3,4,5])
arr_by_tuples = np.array((1,2,3,4,5))

print(arr_by_list, arr_by_tuples)
print(arr_by_list[1], arr_by_list.dtype)

##SCALARS / 0D ARRAY
_0D_arr = np.array(20)
print(_0D_arr, _0D_arr.ndim)

##1D ARRAY
_1D_arr = np.array((1,2,3,4,5,6,7,8))
print(_1D_arr, _1D_arr.ndim, _1D_arr[1])
print(_1D_arr[:4])

##2D ARRAY
_2D_arr = np.array(((1,2,3), (4,5,6)))
print(_2D_arr, _2D_arr.ndim, _2D_arr[0,0])

##3D ARRAY
_3D_arr = np.array((((1,2,3), (4,5,6)), ((7,8,9), (10,11,12))))
print(_3D_arr, _3D_arr.ndim, _3D_arr[0,0,0])

##CREATING ARRAY WITH DIMENSIONS SPEC
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr, arr.ndim, arr[0,0,0,0,1])

##ARRAY TYPES
int_arr = np.array([1,2,3], dtype='i')
float_arr = np.array([1,2,3], dtype='f')
Str_arr = np.array([1,2,3], dtype='S')
UniStr_arr = np.array([1,2,3], dtype='U')

print(int_arr, int_arr.dtype)
print(float_arr, float_arr.dtype)
print(Str_arr, Str_arr.dtype)
print(UniStr_arr, UniStr_arr.dtype)

new_arr = float_arr.astype(int)
print(new_arr, new_arr.dtype)

##COPY/VIEW 
copy_arr = new_arr.copy()
view_arr = new_arr.view()

copy_arr[0] = 10
print(new_arr, copy_arr)
print("==>", copy_arr.base)

view_arr[0] = 100
print(new_arr, view_arr)
print("==>", view_arr.base)

##SHAPEVIEW OF ARR DIMENSIONS
print(_0D_arr.shape, _1D_arr.shape, _2D_arr.shape, _3D_arr.shape)

##RESHAPING ARRAYS
print(arr_by_tuples.reshape(5, 1))