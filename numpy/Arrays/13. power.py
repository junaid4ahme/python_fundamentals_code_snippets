import numpy as np
# CREATING ARRAYS
a1 = np.array([2, 4, 6, 8, 10])
a2 = np.array([3, 6, 9, 12, 15])
a3 = np.zeros(4, dtype=int)
a4 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])

# PRINTING ARRAYS
print("a1:   ", a1, "\na2:   ", a2, "\na3:   ", a3, "\na4:   ", a4)
print("\n\n")

# POWER OF AN ARRAY
# can be used to square or square root the given array
p1 = np.power(a1, 2)
print(p1)
print("\n\n")

p2 = p1.astype(float)
print(p2)
print("\n\n")

p3 = p1 + 0.65
print(p3)

