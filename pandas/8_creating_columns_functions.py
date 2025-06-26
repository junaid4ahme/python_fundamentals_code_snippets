import pandas as pd

mydict = {'empid': ['1001', '1002', '1003', '1004', '1005'],
          'fname': ['Ahmar', 'Arhan', 'Waleed', 'Musavvir', 'Nameerah']}

df = pd.DataFrame(mydict)
print(df, '\n\n')

df['salary'] = [50000, 40000, 60000, 78000, 35000]
# You can also use this code if you like
# df.insert(loc=2, column='salary', value=[50000, 40000, 60000, 78000, 35000])
print(df, '\n\n')

df['tax'] = df['salary'] * 0.18
print(df, '\n\n')

# YOU CAN USE LAMBDA FOR THE SAME
# assign is used to create column it's the only method where we don't need the quotation mark
# we can create multiple columns with multiple functions using assign METHOD
# location attribute wont work here
df = df.assign(pf=lambda x: x.salary * 0.12)
print(df, '\n\n')

# Let's make gross salary column
df = df.assign(gross=lambda x: x.salary - x.pf - x.tax)
print(df, '\n\n')

df = df.assign(cutting=lambda b: b.tax + b.pf)
print(df, '\n\n')


