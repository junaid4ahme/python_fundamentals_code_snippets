import numpy as np
# MATRICES ARE SIMILAR TO ARRAYS
# THERE ARE TWO METHODS TO CREATED MATRICES

# 1_poc.py. CREATING A MATRIX USING STRING:
from numpy import matrix

str1 = '1_poc.py 2 3 4 5 6 7 8 9'
m1 = matrix(str1)

print(m1)

# 2. CREATING MATRIX USING ARRAY:
a1 = np.array([[1,2], [2, 1]])

m2 = np.matrix(a1)
print(m2)

# 3. CREATING MATRIX USING DIRECT METHOD
m3 = np.matrix([[1, 3], [5, 89]])
print(m3)



