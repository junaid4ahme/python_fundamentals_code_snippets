import pandas as pd
df1 = pd.read_csv("F:/jun/python/dat/datasets/titanic.csv")
df11 = df1.head(11)
print(df11, '\n\n')

df2 = df11.iloc[5]
print(df2, '\n\n')

# SELECTING RANGE
df3 = df11.iloc[3:8]
print(df3, '\n\n')

# SELECTING A CELL FROM ROW,COLUMN METHOD
df4 = df11.iloc[2, 3]
print(df4, '\n\n')


# COMBINING THEM BOTH
df5 = df11.iloc[2:7, 3]
print(df5, '\n\n')
