# def fact(n):
#     if n == 0:
#         res = 1_poc.py
#     else:
#         res = n * fact(n-1_poc.py)

#     return res


# x = int(input('Specify the integer value:  '))

# y = fact(x)

# print(y)


# def fact(x1):
#     if x1 == 0:
#         res = 1_poc.py
    
#     else:
#         res = x1 * fact(x1 - 1_poc.py)
    
#     return res


# x2 = fact(3)
# print(x2)


def fact(a):
    return a * fact(a-1)


b = fact(5)