# JOINING COLUMNS WITHOUT COMMON NAME
# JOINING ON THE BASIS OF COMMON DATA
import pandas as pd

# CREATING DATAFRAMES
playersage = pd.DataFrame({'Player Name': ['Rahul Dravid', 'Virendar Sehwag', 'Irfan Pathan'],
                          'Age': [30, 34, 28]})
playersalary = pd.DataFrame({'Sportsman Name': ['Rahul Dravid', 'Yuvraj Singh', 'Irfan Pathan'],
                             'Salary (Lakhs)': [50, 40, 25]})

# INNER JOIN WITHOUT COMMON NAME
ij = pd.merge(playersage, playersalary, left_on='Player Name', right_on='Sportsman Name')
print('THE INNER JOIN:-    ')
print(ij, '\n\n')


# LEFT JOIN WITHOUT COMMON COLUMN
lj = pd.merge(playersage, playersalary, left_on='Player Name', right_on='Sportsman Name', how='left')
print('THE LEFT JOIN:-      ')
print(lj, '\n\n')


# CONCATENATING THE DATAFRAMES
cct = pd.concat([playersage, playersalary])
print(cct, '\n\n')

