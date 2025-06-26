# IMPORT NUMPY AS np FOR MORE MANAGEABLE PROGRAM
import numpy as np

# CREATING AN ARRAY:
a1 = np.array([1, 2, 3])
# print(a1)
# print("\n\n\n")

# PRINTING AN ARRAY

# for x in a1:
  #   print(x)


print('a1 = ', a1)
print("\n\n\n")


stmt = 'This is another representation of elements inside the array:'
print(stmt)
for i in a1:
    print(i, end=', ')
