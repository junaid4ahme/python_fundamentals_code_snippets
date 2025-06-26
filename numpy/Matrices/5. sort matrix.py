import numpy as np
# CREATING MATRIX
m1 = np.matrix([[1, 2, 3], [99, 96, 95], [19, 18, 19]])
print(m1)
print("Type:")
print(type(m1))

# SORTING THE MATRIX
srt1 = np.sort(m1)
print(srt1)

srt2 = np.sort(m1, axis=0)
print(srt2)

