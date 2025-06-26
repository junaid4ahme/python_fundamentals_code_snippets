from functools import *

l1 = [20000, 50000, 100000, 30000]

"""
s = 0
for i in l1:
    s = s + i
print(s)
"""


def red1(x, y):
    return x + y


"""
l2 = reduce(red1, l1)
print(l2)
"""


res = reduce(lambda x, y: x + y, l1)
print(res)
