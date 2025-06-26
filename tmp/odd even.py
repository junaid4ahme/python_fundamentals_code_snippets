# create odd and even number list from a list.

list1 = [*(range(1, 51))]
print(list1)

even = []
odd = []

for i in list1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)


# FUNCTION IS A BLOCK OF INSTRUCTIONS THAT ARE WRITTEN TO GET SPECIFIC RESULT.

def sr(x):
    return x ** 2


a = sr(12)
print(a)

