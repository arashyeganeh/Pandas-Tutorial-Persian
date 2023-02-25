import pandas as pd

try:
    df = pd.read_csv('dataset.csv')
    df.fillna(0.0, inplace=True)
    print(df)

except Exception as err:
    print(err)
