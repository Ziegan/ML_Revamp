from math import log

import numpy as np

sample_array = np.arange(1, 10)
print(np.log2(sample_array))
print(np.log10(sample_array))
print(np.log(sample_array))

##LOG AT ANY BASE
nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))
