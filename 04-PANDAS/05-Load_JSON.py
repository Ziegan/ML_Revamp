import pandas as pd

csv_file = pd.read_csv("Data/data_sheet.csv")
csv_file.to_json("Data/data_sheet.json")

json_file = pd.read_json("Data/data_sheet.json")
print(json_file)
