import numpy as np
# CREATING ARRAYS
a1 = np.array([2, 4, 6, 8, 10])
a2 = np.array([3, 6, 9, 12, 15])
a3 = np.zeros(4, dtype=int)
a4 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])

# PRINTING ARRAYS
print("a1:   ", a1, "\na2:   ", a2, "\na3:   ", a3, "\na4:   ", a4)
print("\n\n")

# SORT: SORTS THE VALUES IN AN ARRAY IN ORDER

sr = np.sort(a2)
print(sr)

rev1 = reversed(sr)
print(rev1)
