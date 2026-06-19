import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

pareto_dist = random.pareto(a=2, size=(2, 3))
print(pareto_dist)

##VISUALIZING PARETO DIST
sns.displot(random.pareto(a=2, size=1000))
plt.show()
