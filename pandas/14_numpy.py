import pandas as pd
import numpy as np
q = np.random.randint(0, 50, (5, 5))
print(q)

df = pd.DataFrame(data=np.random.randint(10, 99, (5, 5)),
                  columns=('T1', 'T2', 'T3', 'T4', 'T5'),
                  index=('stu1', 'stu2', 'stu3', 'stu4', 'stu5'))
print(df)


s1 = df < 50
print(s1, '\n\n')

s2 = df.where(df > 40, 'Fail')
print(s2, '\n\n')

