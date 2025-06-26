# IMPORTING THE PANDAS
import pandas as pd

# CREATING A DICTIONARY OR MAP
mydict1 = {'id': [1, 2, 3, 4, 5, 6, 7, 8],
           'person': ['Jack', 'Henry', 'Jonah', 'John', 'Geralt', 'Legolas', 'Din', 'Altair'],
           'franchise': ['Pirates of the Caribbean', 'Horrid Henry', 'Jonah Hex', 'Constantine', 'The Witcher',
                         'Tolkien', 'The Mandalorian', 'Assassins Creed']}

# CONVERTING THE DICTIONARY INTO DATA-FRAME
df = pd.DataFrame(mydict1)

# CREATING SUBSET ON COLUMNS
sd = df['franchise']
print(sd)
print('\n\n')


# CREATING SUBSET BASED ON CONDITIONS
ss = df[df['id'] > 3]
print(ss)
print('\n\n')


# CREATING THE SUBSET BASED ON TWO CONDITIONS
s = df[df['id'] > 4][df['person'] == 'Altair']   # don't use comma between two conditions
print(s)
print('\n\n')


# CREATING SUBSET INTO SPECIFIC RANGE OF ROWS (SLICING THE DATA)
print('Data frame of range 0:4 ')
s1 = df[0:4]
print(s1)
print('\n\n')

print('Data Frame on range of 0:8')             # the last number in the range is included while creating subset
s2 = df[0:8]
print()
print(s2)
