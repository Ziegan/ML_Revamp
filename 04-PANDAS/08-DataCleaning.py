import pandas as pd

raw_data = pd.read_csv("Data/Missing_Data.csv")
print(raw_data)

##REMOVING NULL/EMPTY VALUES
Cleaned_DF = raw_data.dropna()
print(Cleaned_DF)

##REPLACE NULL/EMPTY VALUES
Filled_DF = raw_data.fillna("Ziegan")
print(Filled_DF)

##REPLACE USING MEAN/MEDIAN/MODE
# MEAN
mean_value = raw_data["Calories"].mean()
print("Mean Value is: ", mean_value)
Mean_Filled = raw_data.fillna({"Calories": mean_value})
print(Mean_Filled)

# MEDIAN
median_value = raw_data["Calories"].median()
print("Median Value is: ", median_value)
Median_Filled = raw_data.fillna({"Calories": median_value})
print(Median_Filled)

# MODE
mode_value = raw_data["Calories"].mode()
print("Mode Value is: ", mode_value)
Mode_Filled = raw_data.fillna({"Calories": mode_value})
print(Mode_Filled)
