import pandas as pd

print(pd.options.display.max_rows)
data = {
    "BIKES": ["SPORTS", "COMMUTER", "HYBRID", "ADVENTURER", "CAFE RIDER"],
    "PRICE": ["2x", "1x", "1.5x", "3x", "2.5x"],
}
data = pd.DataFrame(data)
data.to_csv("Data/data_sheet.csv")

read_data = pd.read_csv("Data/data_sheet.csv")
print(read_data.to_string())
