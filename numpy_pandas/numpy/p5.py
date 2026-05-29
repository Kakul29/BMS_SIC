import numpy as np

array1 = np.full((2, 4), 5)
print(array1)
array2 = np.full((1,5), 10)
# Here array2 is still a ndarray
print(type(array1[1][1]))
print(type(array1))
