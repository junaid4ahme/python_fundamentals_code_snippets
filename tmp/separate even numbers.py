
d1 = {"a":1, "b":2, "c":3, "d":4}

str1 = str(d1)
for i in str1:
    if i.isnumeric():
        print(i)
    elif i.isalpha():
        print(i)

