import matplotlib.pyplot as plt
import pandas as pd

raw_data = pd.read_csv("Data/data.csv")

##NORMAL PLOTTING
raw_data.plot()
plt.show()

##SCATTER PLOTTING
raw_data.plot(kind="scatter", x="Duration", y="Calories")
plt.show()

raw_data.plot(kind="scatter", x="Duration", y="Maxpulse")
plt.show()

##HISTOGRAM PLOTTING
raw_data["Duration"].plot(kind="hist")
plt.show()
