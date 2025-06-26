# IMPORTING THE PANDAS
import pandas as pd

# CREATING A DICTIONARY OR MAP
mydict1 = {'id': [1, 2, 3, 4, 5, 6, 7, 8],
           'person': ['Jack', 'Henry', 'Jonah', 'John', 'Geralt', 'Legolas', 'Din', 'Altair'],
           'franchise': ['Pirates of the Caribbean', 'Horrid Henry', 'Jonah Hex', 'Constantine', 'The Witcher',
                         'Tolkien', 'The Mandalorian', 'Assassins Creed']}
# CREATING DATAFRAME BASED ON DICTIONARY
df = pd.DataFrame(mydict1)

# CREATING SUBSET BASED ON QUERY
#  Query should be in quotation marks

a = df.query('id < 3')
print(a)
print()

b = df.query('id >= 7')
print(b)
print()

c = df.query('franchise in ["Assassins Creed", "The Witcher", "Tolkien"]')
print(c)
print()

d = df.query('franchise != ["Tolkien", "Jonah Hex"]')
print(d)
print()

e = df.query('franchise in ["Tolkien"]')
print(e)
print()


f = df.query('franchise in ["Assassins Creed"]')
print('Only Assassin\'s Creed')
print(f)

