import pandas

print(pandas.__version__)
mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}

dataframe = pandas.DataFrame(mydataset)
print(dataframe)
