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

# CONCATENATING THE TABLES
# SYNTAX: pd.concat([dataframe1,dataframe2],ignore_index=true])

cat = pd.concat([df1, df2])
print(cat, '\n\n')     # if column names are same then the tables are added below the base table

# SORTING THE INDEX
cat1 = pd.concat([df1, df2], ignore_index=True,)
print('CONCAT IGNORE INDEX OF SECOND TABLE OR REINDEX')
print(cat1, '\n\n')

# CONCATENATING TABLES SIDE BY SIDE
cat2 = pd.concat([df1, df2], axis=1)
print('CONCAT SIDE BY SIDE')
print(cat2, '\n\n')

# APPENDING DATAFRAMES
ap = df1.append(df2)   # append method is deprecated and removed out of the futures pandas updates
print(ap, '\n\n')

