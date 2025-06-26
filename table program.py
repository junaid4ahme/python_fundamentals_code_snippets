#  WRITE A PROGRAM THAT WILL RETURN THE TABLE OF THE GIVEN INPUT.

t = []

a = int(input("Insert the number here:   "))
b = a
while len(t) < 10:
    t.append(b)
    b = a + b

print(t)

