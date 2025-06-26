import pandas as pd

# CREATING DATAFRAME FROM A TUPLE

tpl = ((1001, 'Nagesh'), (1002, 'Lakshmi'), (1003, 'Ganesh'))
for i in tpl:
    print(i)
print('\n \n')

# CONVERTING GIVEN TUPLE INTO DATAFRAME
df = pd.DataFrame(tpl)
print('Data Frame: \n', df)
print('\n\n')

# WE CAN ADD NAMES TO THE COLUMNS
df.columns = ['eid', 'fname']
print('Data Frame: \n', df)

# WE CAN RENAME THE COLUMNS
df.rename(columns={'eid': 'empid'}, inplace=True)
print('Renamed Data Frame: \n', df)

# WE CAN ADD NEW COLUMNS
df['dept'] = ['Sales', 'HR', 'Production']
print('\n\n', df)

df['Gender'] = ['Male', 'Female', 'Male']
print('\n\n', df)

# WE CAN INSERT THE COLUMNS IN A SPECIFIC INDEX PLACE
df.insert(column='Salary', value=[10000, 12000, 15000], loc=3)
print('\n\n', df)
