import pandas as pd

dataSet = [
    "Arash",
    "Shahram",
    "Omid",
    "Morteza",
    "Najme",
    "Mahsa",
    "Elham",
    "Maryam",
    "Sanam",
]

series = pd.Series(dataSet)
print(series)
print(series[0])
