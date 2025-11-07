import pandas as pd
import numpy as np

ser = pd.Series(np.random.rand(34))
print('\nDatatype is:\n',type(ser))
print(ser)

newdf = pd.DataFrame(np.random.rand(334,5) , index=np.arange(334))
newdf.to_csv('Data2.csv')
print('\n\nNew Data Frame:\n',newdf)
print('\n\nDescribe:\n',newdf.describe())

print('\n\n1st 5 entries:\n',newdf.head())     #1st 5 entries unless (no of entries needed)
print('\n\nLast 5 entries:\n',newdf.tail())     #last 5 entries unless (no of entries needed)

print('\n\nDatatypes in data frame:\n',newdf.dtypes)

newdf[0][0]='Nikshay'
print('\n\nManipulated entries dataypes:\n',newdf.dtypes)     #Column 0 is now object as 1 entry is string

print('\n\nIndices:\n',newdf.index)

print('\n\nColumns:\n',newdf.columns)

#Change datatype back to float
newdf[0][0]=0.35

#Converts to numpy array
newdf.to_numpy()
print('\n\nConverted to numpy:\n',newdf)

#Transpose
print('\n\nTranspose:\n',newdf.T)

#Sort to descending in columns
newdf.sort_index(axis=1 , ascending=False, inplace=True)
print('\n\nSort to descending in columns:\n',newdf)
#axis=0 -->sorts rows , axis=1 --> sorts columns
print('\n\n0th Column:\n',newdf[0])
print()