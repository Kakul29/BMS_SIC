import numpy as np

array1 = np.full((2, 4), 5, dtype=int)
print(array1)
print(type(array1))
print(type(array1[1][1]))

array1 = np.full((2, 4), 5, dtype=np.float64)
print(array1)
print(type(array1))
print(type(array1[1][1]))
