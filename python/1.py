# REVERSE THE GIVEN STRING:
# Using strip() Method

istr = str(input("INSERT STRING HERE:   "))


def reverser1(x):
    l1 = x.strip()
    l2 = reversed(l1)
    l3 = []
    for i in l2:
        l3.append(i)
    return l3


res = reverser1(istr)
print(res)
print(''.join(res))

