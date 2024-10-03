import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(-5, 10, 100000) > 0

plt.pie(x)
plt.show()
