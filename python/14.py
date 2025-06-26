# COUNT REPEATED ELEMENTS IN THE LIST
l1 = [1, 1, 3, 4, 6, 7, 6, 5, 4, 6, 9]


def counter1(x):
    s1 = set(x)
    for i in s1:
        n = l1.count(i)
        print(i, n)


counter1(l1)

