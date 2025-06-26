import numpy as np

a1 = np.arange(1, 10)
a2 = np.array([[2, 4, 6], [3, 6, 9], [4, 8, 12]])

# RESHAPE:
# THERE IS LIMITATION ON NUMBER OF ELEMENTS CANT CREATE 3X3 ARRAY WITH JUST 8 NUMBER OF ELEMENTS
rsh = a1.reshape(3, 3)
print(rsh)
print("\n\n")

# FLATTEN: USED TO FLATTEN THE MULTI DIMENSIONAL ARRAY
flt = a2.flatten()
print(a2)
print(flt)
