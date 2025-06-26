# IMPORTING THE PANDAS
import pandas as pd


# CREATING A DICTIONARY OR MAP
mydict = {'id': [1, 2, 3, 4, 5, 6, 7, 8],
          'person': ['Jack', 'Henry', 'Jonah', 'John', 'Geralt', 'Legolas', 'Din', 'Altair'],
          'franchise': ['Pirates', 'Henry', 'Hex', 'Constantine', 'Witcher', 'Tolkien', 'Mandalorian', 'Assassins']}


# CONVERTING THE DICTIONARY INTO DATA-FRAME
df = pd.DataFrame(mydict)


# FINDING THE NUMBER OF COLUMNS
print('The columns in the dataframe are \n ', df.columns)


# FINDING THE SIZE OF THE DATAFRAME
print('\nThe number of rows indexed in the dataframe are \n ', df.index)
