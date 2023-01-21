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

series = pd.Series(dataSet, index=["a", "b", "c", "d", "e", "f", "g", "h", "y"])
print(series)
print(series["b"], series[1])  # series["b"] = series[1]
