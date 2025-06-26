import pandas as pd
tpl1 = (('Eminem', 'Rapper'), ('Ed Sheeran', 'Singer'), ('Robert De Nero', 'Actor'), ('Kevin Hart', 'Comedian'))
df1 = pd.DataFrame(tpl1)
print(df1, '\n\n')

df1.columns = ['NAME', 'CRAFT']
print(df1, '\n\n')

df1.insert(loc=0, column='SR.', value=(1, 2, 3, 4))
print(df1, '\n\n')

df1['BEST'] = ['Rap God', 'Shape of You', 'Irishman', 'Grandpa Stare']
print(df1, '\n\n')
