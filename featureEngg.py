import pandas as pd
data={'candy variety':['chocolate hearts','sour jelly','candy canes','sour jelly','fruit drops'],
	'Date and Time':['09-02-2020 14:05','24-10-2020 18:00','18-12-2020 20:13','25-10-2020 10:00','18-10-2020 15:46'],
	'Day':['sunday','saturday','friday','sunday','sunday'],
	'Length':[3,3.5,3.5,3.5,3],
	'Breadth':[2,2,2.5,2,3],
	'Price':[7.5,7.6,8,7.6,9]}
df=pd.DataFrame(data)
df['Date and Time']=pd.to_datetime(df['Date and Time'],format="%d-%m-%Y %H:%M")
print(df)
print('\n')

print('# creating new feature Date from existing feature Date and Time #')
print('\n')
df['Date']=df['Date and Time'].dt.date
print(df[['candy variety','Date']])

print('\n')
print('# creating weekend from days #')
import numpy as np
df['weekend']=np.where(df['Day'].isin(['saturday','sunday']),1,0)
print(df[['candy variety','Date','weekend']])


print('\n')
print('# Appending row with missing values #')
#Appending row with missing values
data={'candy variety':['chocolate hearts','sour jelly','candy canes','sour jelly','fruit drops'],
	'Date and Time':['09-02-2020 14:05','24-10-2020 18:00','18-12-2020 20:13','25-10-2020 10:00','18-10-2020 15:46'],
	'Day':['sunday','saturday','friday','sunday','sunday'],
	'Length':[3,3.5,3.5,3.5,3],
	'Breadth':[2,2,2.5,2,3],
	'Price':[7.5,7.6,8,7.6,9]}
df=pd.DataFrame(data)
df['Date and Time']=pd.to_datetime(df['Date and Time'],format="%d-%m-%Y %H:%M")
df.loc[len(df.index)]=[np.NaN,'22-10-2020 17:24','thursday',3.5,2,np.NaN]
print(df)

print('\n')
print('# Imputation #')
df['candy variety']=df['candy variety'].fillna(df['candy variety'].mode()[0])
df['Price']=df['Price'].fillna(df['Price'].mean())
print(df)

print('\n')
print('# Discretization #')
df['Type of Day']=np.where(df['Day'].isin(['saturday','sunday']),'weekend','weekday')
df[['candy variety','Day','Type of Day']]
print(df)

print('\n')
print('# Categorical Encoding #')
for x in df['Type of Day'].unique():df[x]=np.where(df['Type of Day']==x,1,0)
print(df[['candy variety','Day','Type of Day','weekend','weekday']])


print('\n')
print('# Feature Splitting #')
df['Date and Time']=pd.to_datetime(df['Date and Time'])
df['Date']=df['Date and Time'].dt.date
print(df[['candy variety','Date']])

