import numpy as np

datas = np.arange(1, 7 * 12 + 3 + 1, 1)
dado = np.loadtxt(".\\dados\\apples_ts.csv", delimiter=",", usecols=datas)

dado_transposto = dado.T
precos = dado_transposto[:, 1:6]
Moscow = precos[:, 0]

Y = Moscow
X = datas
n = np.size(Moscow)

# Coeficiente ângular:
a = (n * np.sum(X * Y) - np.sum(X) * np.sum(Y)) / (n * np.sum(X**2) - np.sum(X) ** 2)

# Coeficiente linear:
b = np.mean(Y) - a * np.mean(X)

np.random.randint(low=40, high=100, size=100)

coef_angulares = np.random.uniform(low=0.10, high=0.90, size=100)

coef_angulares[2] * X + b

coef_angulares[29]

norma = np.array([])
for i in range(100):
    norma = np.append(norma, np.linalg.norm(Moscow - (coef_angulares[i] * X + b)))

np.min(norma)

norma[29]
norma
