import numpy as np

##PI VALUE
print(np.pi)

##DEGREES
sin = np.sin(np.pi / 2)
cos = np.cos(np.pi / 2)
tan = np.tan(np.pi / 2)
print(sin, cos, tan)

sin_array = np.sin(np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5]))
cos_array = np.cos(np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5]))
tan_array = np.tan(np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5]))
print(sin_array, cos_array, tan_array)

##DEGREES TO RADIANS
print(np.deg2rad(sin))

##RADIANS TO DEGREES
print(np.rad2deg(np.deg2rad(sin)))

##FINDING ANGLES
print(np.arcsin(1.0), np.arccos(1.0), np.arctan(1.0))
print(np.arcsin(sin_array), np.arccos(cos_array), np.arctan(tan_array))

##FINDING HYPOTENUES
base = 3
perp = 4
print(np.hypot(base, perp))
