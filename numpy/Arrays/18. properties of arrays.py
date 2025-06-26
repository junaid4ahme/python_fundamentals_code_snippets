# OBJECTS
import numpy as np
a1 = np.array([[1, 2, 3], ['Joe', 'Jack', 'Jill'], [50, 80, 65]])
a3 = np.linspace(0, 12, 5)

print("DATA:")
print(a1)
print("\n")
print(a3)
print("\n")

# 1_poc.py. OBJECT TYPE:
print("Object Type:")
print(type(a1))


# 2. DATA TYPE:
print("Data Type:")
print(a1.dtype)


# 3. DIMENSION OF ARRAY
print("Dimension of the array:")
print(a1.ndim)


# 4. SHAPE OF AN ARRAY
print("The shape of Array is:")
print(a1.shape)

# 5. SIZE OF AN ARRAY
print("The size of an array is:")
print(a1.size)

