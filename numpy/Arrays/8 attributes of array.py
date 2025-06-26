import numpy as np
# ATTRIBUTES OF AN ARRAY
a = np.array([1, 3, 4, 8, 9])
a2 = np.array([[1, 2, 4], [5, 4, 8]])

# 1_poc.py. ndim
# IT SHOWS THE DIMENSIONS OF AN ARRAY
v = np.ndim(a)
print(np.ndim(a))

# 2. shape
print("\n\n")
print(np.shape(a))
print(np.shape(a2))

# 3. size: total number of elements
print("\n\n")
print(np.size(a))
print(np.size(a2))


