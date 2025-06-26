# DEEP COPY

# As we know in shallow copy it still keeps the reference to the elements inside elements.
# To avoid this we use deep copy.

from copy import *

nested_list = [[1, 3, 5], [2, 5, 6], [8, 9, 7]]
copy_list = deepcopy(nested_list)

nested_list[0][1] = 1200

print(nested_list)
print(copy_list)


# As you can see we can still keep the object within object as we wanted.
