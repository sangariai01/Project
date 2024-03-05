import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("laptop_price.csv", encoding='latin-1')
df=pd.DataFrame(data)

# print(df)
print(type(df))
print(df.info())

df.plot(kind='line',
         x='Company',
         y='Price_euros',
         color='red')

plt.title("Laptop Price Graph")
plt.show()