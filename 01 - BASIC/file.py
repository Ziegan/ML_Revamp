from pandas import pandas as pd

df  = pd.read_csv('ASHMA.csv')

#printdf.isnull().sum())


#df =  df.rename(columns={"Pulse":"pulse"})
df["Pulse"] = df["Pulse"].astype(str).strip()
print(df)

