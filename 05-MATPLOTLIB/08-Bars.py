import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([-5, -4, -3, -2, -1, 0])

##VERTICAL BARS
plt.bar(x, y, color="Green", width=0.1)
plt.show()

##HORIZONTAL BARS
plt.barh(x, y, color="black", height=0.1)
plt.show()
