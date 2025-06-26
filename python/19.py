
n = 24
flag = True

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            flag = False
        else:
            pass

print(n, flag)

