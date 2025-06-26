# IMPORTING THE PANDAS

import pandas as pd

# CREATING A DICTIONARY OR MAP

mydict = {'id': [1, 2, 3, 4, 5, 6, 7, 8],
          'person': ['Jack', 'Henry', 'Jonah', 'John', 'Geralt', 'Legolas', 'Din', 'Altair'],
          'franchise': ['Pirates', 'Henry', 'Hex', 'Constantine', 'Witcher', 'Tolkien', 'Mandalorian', 'Assassins']}

# CONVERTING THE DICTIONARY INTO DATA-FRAME

dataframe = pd.DataFrame(mydict)

# PRINTING THE DATA-FRAME

print(dataframe)