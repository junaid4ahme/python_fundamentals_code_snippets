import numpy as np
# SHALLOW COPYING:
# IN SHALLOW COPYING IF WE CHANGE ONE ARRAY OTHER WILL ALSO CHANGE

a1 = np.array([1, 2, 44])
sc = a1.view()
print(sc)


# DEEP COPYING:
# IN DEEP COPYING IF WE CHANGE ONE ARRAY OTHER WILL REMAIN UNAFFECTED.

b1 = np.array([20, 40, 50])
dc = b1.copy()
print(dc)


