import pandas as pd
df1 = pd.read_csv("F:/jun/python/dat/datasets/cities_weather.csv")
print(df1, '\n\n')

# PRINTING DATA THAT IS GROUPED
# GROUPING THE DATA
df2 = df1.groupby('city')

# TO PRINT USE FOR LOOP
for x in df2:
    print(x)

# NOW THAT WE HAVE GROUPS IN DATA FRAMES WE CAN RETRIEVE THE GROUPS
df3 = df2.get_group('paris')
print(df3, '\n\n')

# RETRIEVE MAX OF EACH GROUP
df4 = df2.max()
print(df4, '\n\n')

# RETRIEVE AGGREGATE OF EACH GROUP
df5 = df2.agg('max')
print(df5, '\n\n')

df6 = df2.agg(['max', 'min'])
print(df6, '\n\n')
