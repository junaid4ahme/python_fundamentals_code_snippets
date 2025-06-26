from copy import *


# Consider two lists
parent_list = [1, 2, 4, 4, 56]

child_list = copy(parent_list)

# Let's try changing child list and see the effect.

# child_list[4] = 12
#
# print(parent_list)
# print(child_list)

# You can see change in child list haven't affected its parent.

# Let's try in case of nested lists.

nested_list = [[1, 3, 5], [2, 5, 6], [8, 9, 7]]
copy_list = copy(nested_list)

nested_list[0][1] = 1200

print(nested_list)
print(copy_list)

# as you can see in case of nested list the shallow copy can still keep reference to the elements.

# DEEP COPY

