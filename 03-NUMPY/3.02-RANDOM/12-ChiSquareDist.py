import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

ChiSquare_dist = random.chisquare(df=2, size=(2, 3))
print(ChiSquare_dist)

# VISUALIZATION OF CHI-SQUARE DIST
sns.displot(random.chisquare(df=1, size=1000), kind="kde")
plt.show()
