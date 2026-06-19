import matplotlib.pyplot as plt
import numpy as np

plots = np.arange(0, 20, 3)
font1 = {"family": "serif", "color": "blue", "size": 20}
font2 = {"family": "serif", "color": "darkred", "size": 15}

plt.plot(plots)
plt.title("TRAVEL", fontdict=font1, loc="center")
plt.xlabel("DISTANCE", fontdict=font2)
plt.ylabel("SPEED", fontdict=font2)
plt.grid(color="green", linestyle="--", linewidth=0.5)  ##grid(axis="X/y")
plt.show()
