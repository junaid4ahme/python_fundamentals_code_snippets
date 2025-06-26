import numpy as np
# CREATING ARRAYS
a1 = np.array([2, 4, 6, 8, 10])
a2 = np.array([3, 6, 9, 12, 15])
a3 = np.zeros(4, dtype=int)
a4 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])

# PRINTING ARRAYS
print("a1:   ", a1, "\na2:   ", a2, "\na3:   ", a3, "\na4:   ", a4)
print("\n\n")

# SUM: GIVES SUM OF ALL ELEMENTS

s1 = np.sum(a1)

print(s1)

s2 = sum(a4)
print(s2)

s3 = sum(s2)
print(s3)

s4 = sum(a2)
print(s4)