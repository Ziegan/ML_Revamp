import pandas as pd

raw_data = pd.read_csv("Data/data.csv")
print(raw_data.corr())
