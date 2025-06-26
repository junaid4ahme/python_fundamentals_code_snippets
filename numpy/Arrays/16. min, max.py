import numpy as np
# CREATING ARRAYS
a1 = np.array([2, 4, 6, 8, 10])
a2 = np.array([3, 6, 9, 12, 15])
a3 = np.zeros(4, dtype=int)
a4 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])

# PRINTING ARRAYS
print("a1:   ", a1, "\na2:   ", a2, "\na3:   ", a3, "\na4:   ", a4)
print("\n\n")

# MIN: GIVES MINIMUM VALUE OF THE ARRAY

mn1 = np.min(a1)
print(mn1)


# MAX: GIVES MAX VALUE IN AN ARRAY
mx1 = np.max(a4)
print(mx1)

