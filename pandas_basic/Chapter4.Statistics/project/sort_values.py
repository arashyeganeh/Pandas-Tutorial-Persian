import pandas as pd

try:
    df = pd.read_csv('dataset.csv')
    df.sort_values(['Mathematic'], ascending=False, inplace=True)
    print(df)

except Exception as err:
    print(err)
