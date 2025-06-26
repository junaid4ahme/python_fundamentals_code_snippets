# WORDCOUNT PROGRAM IN PYTHON

str1 = "honor we live in a society where honor is a distant memory"


def wordcount(x):
    l1 = x.split()
    set1 = set(l1)
    for i in set1:
        a = l1.count(i)
        print(i, a)


wordcount(str1)
