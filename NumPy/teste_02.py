import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1, 1.0001, 0.0001)

y1 = np.sqrt(1 - x**2)
y2 = -np.sqrt(1 - x**2)


plt.plot(x, y1, "r")
plt.plot(x, y2, "r")
