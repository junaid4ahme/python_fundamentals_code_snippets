import pandas as pd
import numpy as np

df1 = pd.DataFrame(data=np.random.randint(11, 99, (3, 3)),
                   columns=('T1', 'T2', 'T3'),
                   index=('Peter', 'Meg', 'Louis'))
print(df1, '\n\n')

df2 = pd.DataFrame(data=(np.random.randint(11, 99, (3, 3))),
                   columns=('T1', 'T2', 'T3'),
                   index=('Peter', 'Meg', 'Louis'))
print(df2, '\n\n')

s1 = df1.where(df1 > 50, df2)
print(s1)
