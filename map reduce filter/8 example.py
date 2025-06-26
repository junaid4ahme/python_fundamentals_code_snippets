# WRITE A PROGRAM THAT CREATES A LIST FROM LISTS OF FIRST NAME AND LAST NAME
fn = ['Jake', 'Billy', 'Hector', 'Jack', 'James', 'Jimmy']
ln = ['Lockly', 'Kimber', 'Escaton', 'Sparrow', 'Parker', 'Gunn']

# DEFINING FUNCTION


def conc1(x, y):
    return x + " " + y


nm = list(map(conc1, fn, ln))
print(nm)

