import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels=mylabels, shadow=True)
plt.show()


plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
plt.legend(title="Stock Fruits:")
plt.show()
