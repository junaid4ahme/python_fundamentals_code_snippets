# find a pattern inside a string.
# find if string contains the given string or not ??

a = "Hello ! My name is Junaid Ahmed, I am from aurangabad, ive completed my grad in 2018."
b = str(input("enter string here:    "))


def finderer(a1):
    if a1.find(b) >= 0:
        return True
    else:
        return False


x = finderer(a)
print(x)
print(type(x))


