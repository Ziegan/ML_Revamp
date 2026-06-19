import datetime as dt
dt_series = dt.datetime.now()
print(dt_series.year, dt_series.month, dt_series.day)
print(dt_series.strftime("%F %T"))

created_date = dt.datetime(1997, 8, 20)
print(created_date)
print(created_date.strftime("%F"))