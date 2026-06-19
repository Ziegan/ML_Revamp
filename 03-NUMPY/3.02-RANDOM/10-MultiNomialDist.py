import numpy.random as random

##FINDING THE PROBABIBLYT VAL OF DICE ROLED 6 TIMES
multinomal_dist = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(multinomal_dist)