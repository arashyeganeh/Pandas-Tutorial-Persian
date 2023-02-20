import pandas as pd

try:
    df = pd.read_csv('dataset.csv')
    print(df.iloc[0:1])

except Exception as err:
    print(err)
