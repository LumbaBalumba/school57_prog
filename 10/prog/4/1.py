import numpy as np

arr2 = [[1, 2, 3], [4, 5, 7]]
arr1 = [[1, 2, 3], [4, 5, 6]]

arr1 = np.array(arr1)
arr2 = np.array(arr2)

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 ^ arr2)

print(arr1 == arr2)
print((arr1 == arr2).all())
print((arr1 == arr2).any())

print(arr1.shape)
