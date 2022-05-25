import pandas as pd


df = pd.read_csv('historical_prices/eth.csv')
df.columns =[str(i).lower().replace(' ','_') for i in df.columns]
print(df)


#df['date'] = pd.to_datetime(df['date'])
print(df[df['date']>'2020-05-24'])