import pandas as pd

try:
    df = pd.read_csv('dataset.csv')

    print(df['Chemistry'].dtypes)
    df = df.astype({
        'Chemistry': 'int32'
    })
    print(df['Chemistry'].dtypes)

except Exception as err:
    print(err)
