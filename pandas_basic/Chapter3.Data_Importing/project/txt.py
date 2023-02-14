import pandas as pd

try:
    df = pd.read_table('dataset.txt')
    print(df)

except Exception as err:
    print(err)
