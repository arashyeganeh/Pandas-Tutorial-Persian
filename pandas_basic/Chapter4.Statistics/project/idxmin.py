import pandas as pd

try:
    df = pd.read_csv('dataset.csv')
    print(df["Chemistry"].idxmin())  # 5

except Exception as err:
    print(err)

print("-----")

series = pd.Series(data=[10, None, 12, 13, 14])
print(series.idxmin())  # 2
print(series.idxmin(skipna=False))  # nan
