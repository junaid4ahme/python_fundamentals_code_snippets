# FIBONACCI SERIES/SEQUENCE
def fibonaccifunc(x):
    a = 0
    b = 1
    if x == 1:
        print(x)
    else:
        print(a)
        print(b)
        for i in range(2, x):
            c = a + b
            a = b
            b = c
            print(c)


fibonaccifunc(12)

