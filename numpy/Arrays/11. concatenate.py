import numpy as np
# CREATING ARRAYS
a1 = np.array([2, 4, 6, 8, 10])
a2 = np.array([3, 6, 9, 12, 15])
a3 = np.zeros(4, dtype=int)
a4 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])

# PRINTING ARRAYS
print("a1:   ", a1, "\na2:   ", a2, "\na3:   ", a3, "\na4:   ", a4)
print("\n\n")

# OPERATIONS
# 1_poc.py. CONCATENATION
c1 = np.concatenate([a1, a2])
c2 = np.concatenate([a1, a3])
print(c1, "\n", c2)
print("\n\n")




