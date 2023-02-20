import pandas as pd

try:
    df = pd.read_csv('dataset.csv')
    print(df.index)

except Exception as err:
    print(err)
