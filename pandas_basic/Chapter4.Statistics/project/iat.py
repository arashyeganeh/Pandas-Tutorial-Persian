import pandas as pd

try:
    df = pd.read_csv('dataset.csv')
    print(df.iat[1, 0])

except Exception as err:
    print(err)
