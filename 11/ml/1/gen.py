import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = np.linspace(-2, 7, 10)

y = 2 * x**2 + 3
y += np.random.normal(0.0, 15.0, y.shape[0])


def reg(n, x_new):
    model = LinearRegression(n_jobs=-1)
    X = np.column_stack([x**i for i in range(1, n + 1)])
    model.fit(X, y)
    X_test = np.column_stack([x_new**i for i in range(1, n + 1)])
    return model.predict(X_test)


x_new = np.linspace(-2, 7, 1000)
y1 = reg(1, x_new)
y2 = reg(2, x_new)
y11 = reg(11, x_new)

plt.scatter(x, y)
plt.plot(x_new, y1, color="r")
plt.plot(x_new, y2, color="g")
plt.plot(x_new, y11, color="b")
plt.savefig("overfitting.png")

plt.show()
