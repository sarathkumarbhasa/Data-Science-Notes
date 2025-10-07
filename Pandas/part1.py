import pandas as pd
import numpy as np

df = pd.read_csv('hotel-booking-data.txt', delimiter='\t')
df.head()

df.describe()

df['Company'].value_counts()

df.dropna()

df['2xRoom'] = df['Room number'] * 2
df

df.dropna(inplace=True)
df

df['Room number'].isna()

df.plot()

df.info()

import pandas as pd
import numpy as np

data = [1, 2, 3, 4, 5]
series = pd.Series(data)
series

data = [10, 20, 30, 40, 50]
custom_index = ['A', 'B', 'C', 'D', 'E']
series = pd.Series(data, index=custom_index)
print(series)
print(series[4])

data = {
    'Name': ['Sarath', 'Kumar', 'Sai', 'Mohith', 'Zunaid'],
    'Age': [19, 18, 17, 16, 15]
}
d1 = pd.DataFrame(data)
print(d1)

print(d1['Name'])
print(d1.loc[0])

df = pd.read_csv('hotel-booking-data.txt', delimiter='\t')
print(df)

print(df.head())
print(df.tail())

df.info()

df.describe()

print(df.shape)
print(df.isna())
print(df.isna().sum())

df.fillna(20, inplace=True)
df.head()

df.drop_duplicates(inplace=True)
df

df.rename(columns={'Company': 'Com Name'}, inplace=True)
df

df.corr()
