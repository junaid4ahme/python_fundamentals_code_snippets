# THERE ARE 4 TYPES OF JOINS INNER JOIN, LEFT JOIN, RIGHT JOIN AND FULL OUTER JOIN
# JOINS ARE USED TO COMBINE TWO TABLES AND GET THE DATA FROM THE COMBINED TABLE

# CREATING DATA FRAMES

import pandas as pd
dict1 = {'player name': ['Rahul Dravid', 'Virendar Sehwag', 'Irfan Pathan'],
         'age': [25, 29, 23]}
df1 = pd.DataFrame(dict1)
print(df1, '\n\n')

dict2 = {'player name': ['Rahul Dravid', 'Yuvraj Singh', 'Irfan Pathan'],
         'salary': [5000000, 4500000, 2500000]}
df2 = pd.DataFrame(dict2)
df2['role'] = ['Captain', 'Vice Captain', 'Player']
print(df2, '\n\n')


# INNER JOIN
# WE ARE USING MERGE COMMAND SINCE JOIN COMMAND MIGHT GET SOME BUGS OR MIGHT BE SLOWER
# SYNTAX:  pd.merge(dataframe1, dataframe2, on = 'primary key')

ij = pd.merge(df1, df2, on='player name')
# WE ARE NOT USING how ATTRIBUTE HERE BECAUSE MERGE IS BY DEFAULT INNER JOIN
print('THE INNER JOIN:- ')
print(ij, '\n\n')

# LEFT JOIN:
# HERE WE CAN JOIN A TABLE TO THE LEFT TABLE OF QUERY
# MEANS LEFT TABLE IS ACTING AS BASE AND RIGHT TABLE IS JOINING TO IT
# SYNTAX: pd.merge(dataframe1, dataframe2, on='primary key', how='left')

lj = pd.merge(df1, df2, on='player name', how='left')
print('THE LEFT JOIN:-  ')
print(lj, '\n\n')

# RIGHT JOIN:
# HERE WE CAN JOIN TWO TABLES WHERE RIGHT SIDE TABLE WILL ACT AS REFERENCE AND ON THE BASIS OF PRIMARY KEY OF
# RIGHT TABLE LEFT TABLE IS JOINED TO IT.
# SYNTAX: pd.merge(dataframe1, dataframe2, on='primary key', how='right')

rj = pd.merge(df1, df2, on='player name', how='right')
print('THE RIGHT JOIN')
print(rj, '\n\n')

# FULL OUTER JOIN:
# HERE WE CAN JOIN TWO TABLES IN SUCH A WAY THAT DATA OF BOTH TABLES WILL BE SHOWN
# SYNTAX: pd.merge(df1, df2, on='primary key', how='outer')

oj = pd.merge(df1, df2, on='player name', how='outer')
print('THE OUTER JOIN:-  ')
print(oj, '\n\n')
