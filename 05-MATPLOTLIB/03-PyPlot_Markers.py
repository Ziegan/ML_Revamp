import matplotlib.pyplot as plt
import numpy as np

###SINGLE AXIS PLOTTING
plots = np.array([1, 3, 5, 7, 9])

##MARKER WITH o
plt.plot(plots, marker="o")  ## || plt.plot(plots, "o")
plt.show()

##MARKER WITH *
plt.plot(plots, marker="*")  ## || plt.plot(plots, "*")
plt.show()

##MARKER WITH FORMATTING 'marker|line|color'
plt.plot(plots, "*:g")  ## || plt.plot(plots, "*")
plt.show()

##MARKER WITH MARKER SIZE/COLOR
plt.plot(plots, marker="*", ms=20, mec="r", mfc="k")
plt.show()
