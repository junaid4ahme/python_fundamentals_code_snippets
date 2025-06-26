import pandas as pd
df1 = pd.read_csv("F:/jun/python/dat/datasets/titanic.csv")
df11 = df1.head(11)
print(df11, '\n\n')


# SELECTING ONLY ONE COLUMN
df2 = df11['Fare']
print(df2, '\n\n')

# SELECTING MULTIPLE COLUMNS
df3 = df11[['Name', 'Sex']]
print(df3)

