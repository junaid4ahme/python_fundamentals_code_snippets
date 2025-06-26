# FIND OUT IF THE GIVEN ARRAY IS MONOTONICALLY INCREASING OR NOT.

import numpy as np

a = np.array([[1, 2, 5, 4], [4, 5, 6, 7]])

# b = np.diff(a) > 0
# print(b)

c = np.all(np.diff(a) > 0)
print(c)
