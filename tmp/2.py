str1 = "a3b3c1"
res = ""
l1 = [i for i in str1]
for i in l1:
    if i.isalpha():
        s = i
    else:
        n = int(i)
        s = s*n
        res = res + s
print(res)
