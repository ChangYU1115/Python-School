from efficient_apriori import apriori
import pandas as pd

df = pd.read_csv('Market_Basket_Optimisation.csv', header= None)
df.head()

transactions = []
for i in range(0, len(df)):
  transactions.append([str(j) for j in df.iloc[i,:] if str(j)!='nan'])

len(transactions)