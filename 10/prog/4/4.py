import numpy as np

A = np.array([[1, 2], [2, 3]])
b = np.array([3, 5])

"""
x + 2y = 3
2x + 3y = 5
"""

print(np.linalg.solve(A, b))
