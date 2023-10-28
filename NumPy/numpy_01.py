import numpy as np
import matplotlib.pyplot as plt

datas = np.arange(1, 7 * 12 + 3 + 1, 1)
dado = np.loadtxt(".\\dados\\apples_ts.csv", delimiter=",", usecols=datas)

dado.ndim

dado.size

dado.shape

dado_transposto = dado.T


precos = dado_transposto[:, 1:6]

plt.plot(datas, precos[:, 0])


Moscow = precos[:, 0]
Kaliningrad = precos[:, 1]
Petersburg = precos[:, 2]
Krasnodar = precos[:, 3]
Ekaterinburg = precos[:, 4]

Moscow
plt.plot(datas, Kaliningrad)

Moscow.shape

Moscow_ano1 = Moscow[0:12]
Moscow_ano2 = Moscow[12:24]
Moscow_ano3 = Moscow[24:36]
Moscow_ano4 = Moscow[36:48]

anoIndice = np.arange(1, 13, 1)
plt.plot(anoIndice, Moscow_ano1)
plt.plot(anoIndice, Moscow_ano2)
plt.plot(anoIndice, Moscow_ano3)
plt.plot(anoIndice, Moscow_ano4)
plt.legend(["ano 1", "ano 2", "ano 3", "ano 4"])


np.array_equal(Moscow_ano1, Moscow_ano2)

np.allclose(Moscow_ano3, Moscow_ano4, 10)

plt.plot(datas, Kaliningrad)

sum(np.isnan(Kaliningrad))

Kaliningrad[4] = np.mean([Kaliningrad[3], Kaliningrad[5]])

plt.plot(datas, Kaliningrad)

np.mean(Moscow)
np.mean(Kaliningrad)

X = datas
Y = X * 2 + 80

Moscow - Y

np.sqrt(np.sum(np.power(Moscow - Y, 2)))

np.linalg.norm(Moscow - Y)

Y = X * 0.43 + 80

Y = Moscow
X = datas
n = np.size(Moscow)

plt.plot(datas, Moscow)
plt.plot(X, Y)

# Coeficiente ângular:
a = (n * np.sum(X * Y) - np.sum(X) * np.sum(Y)) / (n * np.sum(X**2) - np.sum(X) ** 2)

# Coeficiente linear:
b = np.mean(Y) - a * np.mean(X)

y = a * X + b

np.linalg.norm(Moscow - y)


plt.plot(datas, Moscow)
plt.plot(41.5, 41.5 * a + b, "r*")
plt.plot(100, 100 * a + b, "r*")
plt.plot(X, y)
