import numpy as np


def dot(arr1, arr2):
    return sum(map(lambda elem: elem[0] * elem[1], zip(arr1, arr2)))


arr1 = np.random.randint(0, 3, (3,))
arr2 = np.random.randint(0, 3, (3,))

print(arr1, arr2)

print(np.dot(arr1, arr2))
print(dot(arr1, arr2))
