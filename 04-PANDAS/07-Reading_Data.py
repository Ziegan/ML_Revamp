import pandas as pd

csv_file = pd.read_csv("Data/customers-100.csv")

print(csv_file.head())  ##print top 5
print(csv_file.head(10))  ##Print top 10
print(csv_file.tail())  ##Print last 5
print(csv_file.tail(10))  ##Print last 10

print(csv_file.info())
