from numpy import random

##PLAIN UNIFORM DIST
uniform_dist = random.uniform(size=(1000))
print(uniform_dist)

##VISUALIZATION
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(uniform_dist, kind="kde")
plt.show()