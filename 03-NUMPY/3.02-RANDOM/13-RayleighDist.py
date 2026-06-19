import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

rayleigh_dist = random.rayleigh(scale=2, size=(2, 3))
print(rayleigh_dist)

##VISUALIZING RAYLEIGH DIST
sns.displot(random.rayleigh(size=1000), kind="kde")
plt.show()
