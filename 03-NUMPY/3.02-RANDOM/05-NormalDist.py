from numpy import random

##PLAIN NORMAL DIST
normal_dist_1 = random.normal(size=(2,3))
print(normal_dist_1)

##NORMAL DIST WITH MEAN and STD DEVIATION
normal_dist_2 = random.normal(loc=1, scale=2, size=(2,3))
print(normal_dist_2)

##VISUALIZATION
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=100), kind="kde")
plt.show()