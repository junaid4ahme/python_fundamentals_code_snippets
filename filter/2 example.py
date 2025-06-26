# write a program that will filter out even numbers from given iterable

l1 = [*range(1, 101)]


def eve1(x):
    if x % 2 == 0:
        return x


o1 = filter(eve1, l1)

l2 = list(o1)
print(l2)
