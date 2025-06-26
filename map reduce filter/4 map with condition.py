# WRITE A PROGRAM THAT FETCHES ONLY THE ODD NUMBERS FROM LIST

# DEFINING A FUNCTION
def oe(x):
    if x % 2 == 0:
        return "{} is Even".format(x)
    else:
        return "Odd"


# CREATING ITERABLE
l1 = [1, 3, 5, 6, 7, 9, 44, 6, 77, 86, 34]


# USING MAP FUNCTION
l2 = list(map(oe, l1))
print(l2)


