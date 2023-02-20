import pandas as pd

try:
    df = pd.read_csv('dataset.csv')
    df_tail = df.tail(2)
    print(df_tail)

except Exception as err:
    print(err)
