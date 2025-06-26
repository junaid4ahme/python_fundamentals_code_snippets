# FILTER FUNCTION
# IT FILTERS OUT THE GIVEN ITERABLE AND CREATE A NEW ITERABLE WITH ELEMENTS SATISFYING THE CONDITION
# syntax:
#          l2 = list(filter(function, list1)

# DEFINING FUNCTION
def fil1(x):
    return x > 4


l1 = [1, 2, 3, 4, 5, 6, 7]

# USING FILTER FUNCTION TO CREATE NEW ITERABLE

l2 = list(filter(fil1, l1))
print(l2)

