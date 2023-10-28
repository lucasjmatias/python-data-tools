import numpy as np
import matplotlib.pyplot as plt


colvalues = np.arange(1, 6)
dados = np.loadtxt(".\\dados\\citrus.csv", delimiter=",", usecols=colvalues, skiprows=1)

dadosLaranjas = dados[:5000, :]

dadosToranjas = dados[5000:, :]


plt.plot(dadosLaranjas[:, 0], dadosLaranjas[:, 1])
plt.plot(dadosToranjas[:, 0], dadosToranjas[:, 1])
plt.legend(["Laranjas", "Toranjas"])
