import pandas as pd

data = {"calories": [100, 200, 300], "duration": [10, 20, 30]}

df = pd.DataFrame(data)
print(df)

##LOCATING ROW 0
print(df.loc[0])
print(df.loc[[0, 1]])  ##LOCATING ROW 0, 1

df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)
