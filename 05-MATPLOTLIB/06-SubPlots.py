import matplotlib.pyplot as plt
import numpy as np

a = np.array([0, 1, 2, 3])
b = np.array([9, 8, 7, 6])
c = np.array([4, 5, 6, 7])
d = np.array([0, -1, -2, -3])

##PLOT 1
plt.subplot(1, 2, 1)
# plt.subplot(2,1,1)
plt.plot(a, b)
plt.title("SAMPLE 1")

##PLOT 2
plt.subplot(1, 2, 2)
# plt.subplot(2,1,2)
plt.plot(c, d)
plt.title("SAMPLE 2")

plt.suptitle("MY EXAMPLES")
plt.show()
