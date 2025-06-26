# LOCATION OF EVEN NUMBERS IN A LIST

lst1 = [1, 3, 2, 9, 8]
for i in lst1:
    if i % 2 == 0:
        print(i, lst1.index(i))
