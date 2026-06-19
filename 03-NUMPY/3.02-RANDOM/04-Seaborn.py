import seaborn as sns
import matplotlib.pyplot as plt

##PLOTTING DISPLOT
sns.displot([1,2,3,4,5])
plt.show()

##PLOTTING WITHOUT DISPLOT
sns.displot([1,2,3,4,5], kind="kde")
plt.show()