import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(5, 0.1, 10000)

plt.hist(x, bins=100)
plt.show()
