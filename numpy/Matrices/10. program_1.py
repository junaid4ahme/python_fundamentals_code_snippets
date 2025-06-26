# Write a program which will create a matrix with specified rows and columns and specified elements
import numpy as np
r, c = [int(i) for i in input('Specify rows and columns Separated by Comma :').split(',')]
print("Number of Rows:", r)
print("Number of Columns:", c)
print("\n\n\n")
l1 = [int(i) for i in input("Specify Elements:\nNote:\nShould be integers. \nSeparated by Comma.\nShould be equal to "
                            "the product of rows and columns.:").split(',')]
l3 = np.array(l1)
l4 = np.reshape(l3, (r, c))

m1 = np.matrix(l4)
print(m1)

m2 = np.transpose(m1)
print("\n\nTranspose of the above matrix:\n", m2)
