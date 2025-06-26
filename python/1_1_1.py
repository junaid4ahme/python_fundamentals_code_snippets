# REVERSE A STRING USING RECURSION METHOD
str1 = "Junaid"


def reverser(x):
    if len(x) == 1:
        return x
    else:
        return reverser(x[1:]) + x[0]


res = reverser(str1)

print(res)
