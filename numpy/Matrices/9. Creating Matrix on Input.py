import numpy as np

x, y = [int(i) for i in input().split(',')]
elem = input("Enter Elements")
m1 = np.matrix(elem)
m2 = np.reshape(m1, (x, y))

print(m1)
print(m2)
