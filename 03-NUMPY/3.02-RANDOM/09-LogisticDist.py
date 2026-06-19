import numpy.random as random
from torch import normal

##PLAIN LOGISTIC DIST
logistic_dist = random.logistic(loc=1, scale=2, size=(100))
print(logistic_dist)

##VISUALIZATION
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(logistic_dist)
plt.show()

##DIFF OF NORMAL TO LOGISTIC
normal_dist = random.normal(scale=2, size=100)

data_points = {"normal": normal_dist, "logistic": logistic_dist}
sns.displot(data_points, kind="kde")
plt.show()