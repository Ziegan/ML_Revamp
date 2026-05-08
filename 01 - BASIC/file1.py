from pandas import pandas as pd

df = pd.read_csv("ASHMA.csv")

#df.isnull().sum()

#df["Pulse"] = df["Pulse"].astype(str).str.replace(" ","")

#df =df.map(lambda x : x.replace(" ","") if isinstance(x,str) else x)
#df = df.dropna()
#df = df.dropna(subset=["Maxpulse"])

#print(df)

#df.columns= df.columns.str.upper()

#df = df.rename(columns={"Pulse":"pulse"})
df["Pulse"] = df["Pulse"].str.upper()
print(df)

