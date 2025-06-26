# FIND OUT IF TWO GIVEN STRINGS ARE ANAGRAMS OR NOT ?

str1 = "pool"
str2 = "loop"


def func1(x, y):
    if set(x) == set(y):
        return True
    else:
        return False


res = func1(str2, str1)
print(res)

res2 = func1("Junaid", "Ahmed")
print(res2)

res3 = func1("pool", "polo")
print(res3)
