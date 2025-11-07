import pandas as pd
import numpy as np

dic1={"name":['a1','b2','c3','d4'], "marks":[98,87,64,43], "Cities":['Mumbai','Chennai','Delhi','Kolkata']}
print(dic1)
df=pd.DataFrame(dic1)
print()
print(df)
print()
df.to_csv('Data1.csv',index=False)

df.index=['1st','2nd','3rd','4th']
print(df)
print()

print(df.describe())
#to access row, use index & for column, the name of column