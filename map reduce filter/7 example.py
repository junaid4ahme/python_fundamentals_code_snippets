# import functools as ft

# DEFINING THE ITERABLE

sal1 = [20000, 30000, 5000, 12000, 40000]

# DEFINING THE FUNCTION


def asal(x):
    return x * 12


asal2 = list(map(asal, sal1))
print(asal2)
