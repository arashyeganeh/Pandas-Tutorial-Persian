import pandas as pd

try:
    df = pd.read_csv('dataset.csv')
    print(df.at[1, 'Name'])

except Exception as err:
    print(err)
