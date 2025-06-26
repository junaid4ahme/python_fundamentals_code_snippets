# FIND OUT THE MISSING ELEMENTS AFTER SUBTRACTING ITERABLE
# for this also we can use set() method

l1 = list(range(1, 11))
print(l1)

l2 = list(range(1, 26))
print(l2)

l3 = set(l2) - set(l1)
l3 = list(l3)
print(l3)


