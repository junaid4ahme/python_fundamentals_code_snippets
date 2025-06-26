# square root using function
def srt(n):
    res = n ** 0.5
    return res


x = int(input('Enter the Integer Value: '))

s = srt(x)
print('The square root of', x, 'is ', s)


# square root of a range
def srt1(n1):
    res = n1 ** 0.5
    return res


r1 = range(1, 11)
for i in r1:
    s1 = srt1(i)
print(s1)

