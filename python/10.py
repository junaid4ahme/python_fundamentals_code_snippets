# FIND OUT IF GIVEN STRIGN IS PALLINDROME OR NOT
str1 = "racecar"


def func1(x):
    if x == x[::-1]:
        return True
    else:
        return False


x = func1(str1)
print(x)




