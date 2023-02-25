import pandas as pd

try:
    df = pd.read_csv('dataset.csv')
    df.dropna(inplace=True)
    print(df)

except Exception as err:
    print(err)
