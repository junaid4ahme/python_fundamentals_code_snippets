import numpy as np
m1 = np.matrix([[1, 2], [10, 11]])
m2 = np.matrix([1, 1])

ad1 = m1 - m2
print(ad1)

m1 = np.matrix([[1, 2], [10, 10]])
m2 = np.matrix([[1, 1], [2, 2]])
sub2 = m1 - m2
print(sub2)
