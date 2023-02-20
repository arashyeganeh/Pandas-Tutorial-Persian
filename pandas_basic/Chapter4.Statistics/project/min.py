import pandas as pd

try:
    df = pd.read_csv('dataset.csv')
    print(df.min())

except Exception as err:
    print(err)
