# input = a3b2f3, output = aaabbfff

str1 = "a2b5s5"
res = ""

for i in str1:
    if i.isalpha():
        x = i
    else:
        n = int(i)
        x = x*n
    res = res+x
print(res)

