# input = aabbbbtttt, output = a2b4c4
from collections import Counter
str1 = "aabbbuuu"
str3 = ""

l1 = [i for i in str1]

d1 = dict(Counter(l1))

str2 = str(d1)

for i in str2:
    if i.isalpha():
        str3 = str3 + i
    elif i.isnumeric():
        str3 = str3 + i
    else:
        pass

print(str3)
