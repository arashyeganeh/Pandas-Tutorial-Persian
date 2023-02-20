import pandas as pd

try:
    df = pd.read_csv('dataset.csv')
    print(df.describe())

except Exception as err:
    print(err)
