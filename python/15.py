# SORT WITHOUT ANY FUNCTION
lst1 = [1, 3, 2, 9, 8]

for i in range(len(lst1)):
    for j in range(i+1, len(lst1)):
        if lst1[i] > lst1[j]:
            lst1[i], lst1[j] = lst1[j], lst1[i]

print(lst1)
