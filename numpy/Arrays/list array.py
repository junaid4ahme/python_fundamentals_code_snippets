import numpy as np
l1 = [*range(1, 21)]
a1 = np.array(l1)
print(a1)
print(type(a1))
a2 = np.reshape(a1, (5, 4))
print(a2)
print(type(a2))
print(a2.shape)
print(a2.ndim)

m1 = np.matrix(a2)
print(m1)
print(type(m1))


