import pandas as pd

try:
    df = pd.read_csv('dataset.csv')
    df_head = df.head(2)
    print(df_head)

except Exception as err:
    print(err)
