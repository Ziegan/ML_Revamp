"""from pandas import pandas as pd

df = pd.read_csv('ASHMA.csv')

df = df.map(lambda x : x.strip() if isinstance(x,str) else x)

print(df)

"""
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def hello():
    print("Hello Ashma")

hello()
