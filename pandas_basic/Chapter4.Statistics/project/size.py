import pandas as pd

try:
    se = pd.Series(['A', 'B', 'C'])
    print(se.size)

    df = pd.read_csv('dataset.csv', na_filter=False)
    print(df)
    print(df.size)

except Exception as err:
    print(err)
