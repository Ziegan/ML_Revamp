import pandas as pd

##SERIES AND LABELS
a = [1, 7, 5, 4]
index_lables = ["a", "b", "c", "d"]
series = pd.Series(a, index=index_lables)
print(series)

##KEY/VALUE PAIR OBJ
weeks = {
    "day1": "Monday",
    "day2": "Tuesday",
    "day3": "Wednesday",
    "day4": "Thursday",
    "day5": "Friday",
}
Series1 = pd.Series(weeks)
print(Series1)

##DICTONARY LABELS
calories = {"day1": 420, "day2": 380, "day3": 390}
Series2 = pd.Series(calories, index=["day1", "day2"])
print(Series2)

##DATAFRAMES
data = {"calories": [1, 2, 3, 4, 5], "duration": [5, 10, 15, 20, 25]}
dataframes = pd.DataFrame(data)
print(dataframes)
