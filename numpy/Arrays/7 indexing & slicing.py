import numpy as np

a = np.arange(1, 10)
a6 = np.array([[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9, 10], [6, 7, 8, 9, 10, 11]])


# SLICING ARRAY
slc = a[2:7]
print("The array is: \n", a, "\nThe Slicing 2:7 is")
print(slc, "\n\n")


# SLICING FROM MULTIDIMENSIONAL ARRAY
slc1 = a6[0:6]

print("the array is:\n", a6)
print("\n\n")
print("They slicing is:/n")
print(slc1)
print("\n\n")


# INDEXING ARRAY
ind = a[0]
print("Indexing \n", "The array is:\n", a)
print("The 0th index is ")
print(ind)
