# write a program which will return all the elements with value more than 100000.
l1 = ['90000', '20000', '120000', '140000', '40000']

o1 = map(int, l1)
l2 = list(o1)


def comp1(x):
    if x > 100000:
        return x


o2 = filter(comp1, l2)

l2 = list(o2)
print(l2)

