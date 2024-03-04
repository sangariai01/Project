import pandas as pd

data=pd.read_csv("laptop_price.csv", encoding='latin-1')

df=pd.DataFrame(data)
# print(df)
# print(df.head())
# print(df.tail())
# print(df.head(10).dropna().to_string())
print(df.tail(10).dropna().to_string())