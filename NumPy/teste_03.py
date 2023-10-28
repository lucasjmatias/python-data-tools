import numpy as np
import matplotlib.pyplot as plt


colvalues = np.arange(1, 6)
dados = np.loadtxt(".\\dados\\citrus.csv", delimiter=",", usecols=colvalues, skiprows=1)

dadosLaranjas = dados[:5000, :]
diametrosLaranjas = dadosLaranjas[:, 0]
pesosLaranjas = dadosLaranjas[:, 1]

dadosToranjas = dados[5000:, :]
diametrosToranjas = dadosToranjas[:, 0]
pesosToranjas = dadosToranjas[:, 1]

plt.plot(diametrosLaranjas, pesosLaranjas)
plt.plot(diametrosToranjas, pesosToranjas)
plt.legend(["Laranjas", "Toranjas"])

Xl = diametrosLaranjas
Yl = pesosLaranjas
nl = np.size(dadosLaranjas)

# Coeficiente ângular:
al = (nl * np.sum(Xl * Yl) - np.sum(Xl) * np.sum(Yl)) / (
    nl * np.sum(Xl**2) - np.sum(Xl) ** 2
)

# Coeficiente linear:
bl = np.mean(Yl) - al * np.mean(Xl)

yl = diametrosLaranjas * al + bl

plt.plot(diametrosLaranjas, yl)
plt.plot(diametrosLaranjas, pesosLaranjas)


Xt = diametrosToranjas
Yt = pesosToranjas
nt = np.size(dadosToranjas)

# Coeficiente ângular:
at = (nt * np.sum(Xt * Yt) - np.sum(Xt) * np.sum(Yt)) / (
    nt * np.sum(Xt**2) - np.sum(Xt) ** 2
)

# Coeficiente linear:
bt = np.mean(Yt) - at * np.mean(Xt)

yt = diametrosToranjas * at + bt

plt.plot(diametrosToranjas, yt)
plt.plot(diametrosToranjas, pesosToranjas)
