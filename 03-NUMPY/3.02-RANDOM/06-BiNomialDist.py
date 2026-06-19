from numpy import random

binomial = random.binomial(n=1, p=0.5, size=2)
print(binomial)

##SAMPLE PROBABILITY CHECK OF A COIN ON 100 FLIPS
probability = {}
for i in range(1, 100): ##FLIPS
    binomial_1 = random.binomial(n=1, p=0.5, size=1) ##0,1 with 50%P returning 1 value
    if binomial_1[0] in probability:
        probability[binomial_1[0]] += 1
    else:
        probability[binomial_1[0]] = 1
print(probability)  ## HASED PROBABILITY SCORE

##VISUALIZE BINOMIAL
import matplotlib.pyplot as plt
import seaborn as sns

binomial_val = random.binomial(n=100, p=0.5, size=100)
sns.displot(binomial_val)
plt.show()

## DIFF TO NORMAL, BINOMIAL

data_plots = {"normal": random.normal(loc=50, scale=5, size=100),
              "binomial": random.binomial(n=100, p=0.5, size=100)}
sns.displot(data_plots, kind="kde")
plt.show()