import numpy as np
radius = 3
x1 = 4
y1 = 4
arraysize = 10
arr = np.zeros((10, 10))
print(arr)
y2, x2 = np.ogrid[0:10, 0:10]
mask = abs(x1-x2) + abs(y1-y2) <= radius
arr[mask] = 1
print(arr)
