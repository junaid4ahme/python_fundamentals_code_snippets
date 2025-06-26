# List Comprehension
# Converting the input into multiple variables
# By default the datatype is string

a, b, c, d = [i for i in input()]
print(a, b, c, d)
print(type(a))

# Feeding specific datatype
e, f, g, h = [int(i) for i in input()]
print(e, f, g, h)

# Showing input Message:
i, j, k, l = [int(i) for i in input("Specify the numbers")]
print(i, j, k, l)

# taking input in split form
m, n, o, p = [int(i) for i in input("specify integers").split(',')]
print(m, n, o, p)