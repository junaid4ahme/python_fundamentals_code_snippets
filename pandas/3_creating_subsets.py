# IMPORTING THE PANDAS
import pandas as pd

# CREATING A DICTIONARY OR MAP
mydict = {'id': [1, 2, 3, 4, 5, 6, 7, 8],
          'person': ['Jack', 'Henry', 'Jonah', 'John', 'Geralt', 'Legolas', 'Din', 'Altair'],
          'franchise': ['Pirates', 'Horrid Henry', 'Hex', 'Constantine', 'Witcher', 'Tolkien', 'Mandalorian', 'Assassins']}

# CONVERTING THE DICTIONARY INTO DATA-FRAME
df = pd.DataFrame(mydict)

# SELECTING COLUMNS OR CREATING SUBSET
a = df[['id']]
# print(a)

# SELECTING MULTIPLE COLUMNS OR CREATING A SUBSET USING MULTIPLE COLUMNS
b = df[['franchise', 'person']]
print(b)
