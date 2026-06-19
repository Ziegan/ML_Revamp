import matplotlib.pylab as plt
import numpy as np

###SIMPLE PLOTS
##LINE PLOTTING SINGLE AXIS
plots = np.array([3, 5, 7, 9, 1, 3])
plt.plot(plots)
plt.show()

##LINE PLOTTING BOTH AXIS
x_points = np.array([0, 5])
y_points = np.array([0, 256])
plt.plot(x_points, y_points)
plt.show()

##WITHOUT LINE PLOTTING
plt.plot(x_points, y_points, "o")
plt.show()

###MULTI POINT PLOTTING
a_plots = np.array([1, 2, 3, 4, 5])
b_plots = np.array([3, 6, 9, 12, 15])
plt.plot(a_plots, b_plots)
plt.show()
