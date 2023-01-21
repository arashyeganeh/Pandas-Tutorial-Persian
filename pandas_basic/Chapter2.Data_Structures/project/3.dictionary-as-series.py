import pandas as pd

dataSet = {"Class-1": "Arash", "Class-2": "Shahram", "Class-3": "Reza"}

series = pd.Series(dataSet, index=["Class-1", "Class-2"])

print(series)
