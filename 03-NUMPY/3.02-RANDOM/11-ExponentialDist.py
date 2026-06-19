import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

expo_dist = random.exponential(scale=2, size=(2, 2))
print(expo_dist)

##VISUALIZING ExponentialDist
sns.displot(random.exponential(size=1000), kind="kde")
plt.show()
