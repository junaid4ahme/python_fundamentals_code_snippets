# FIND OUT DUPLICATES IN THE LIST

l1 = [1, 1, 3, 5, 6, 6, 6, 7, 8, 8, 9, 9]
l2 = [i for i in l1 if l1.count(i) > 1]
l3 = list(set(l2))
print(l3)


