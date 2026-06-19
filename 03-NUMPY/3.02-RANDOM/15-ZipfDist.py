import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

zipf_dist = random.zipf(a=2, size=(2, 3))
print(zipf_dist)

##VISUALIZATION OF ZIPF DIST
sns.displot(random.zipf(a=2, size=1000))
plt.show()
