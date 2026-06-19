import pandas as pd

##CLEANING DATE MISMATCH
raw_data = pd.read_csv("Data/Missing_Data.csv")
raw_data["Date"] = pd.to_datetime(raw_data["Date"], format="mixed")
print(raw_data)

##CLEARNING EMPTY ROW WITHOUT DATE
cleaned_data = raw_data.dropna(subset="Date")
print(cleaned_data)

##REMOVING DUPLICATE DATA
print(cleaned_data.duplicated())
unique_data = cleaned_data.drop_duplicates()
print(unique_data)
