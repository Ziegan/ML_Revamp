from numpy import random
from sympy import binomial

##POISSON DIST
poisson = random.poisson(lam=50, size=1000)
print(poisson)

##VISUALIZATION
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(poisson)
plt.show()

##DIFF OF NORMAL WITH POISSON
normal = random.normal(loc=50, scale=7, size=1000)
data_points = {"normal": normal, "poisson": poisson}
sns.displot(data_points, kind="kde")
plt.show()

## DIFF OF BINOMIAL WITH POISSON
binomial = random.binomial(n=1000, p=0.5, size=1000)
data_points = {"binomial": binomial, "poisson": poisson}
sns.displot(data_points, kind="kde")
plt.show()

## DIFF WITH ALL
data_points = {"normal": normal, "binomial": binomial, "poisson": poisson}
sns.displot(data_points, kind="kde")
plt.show()