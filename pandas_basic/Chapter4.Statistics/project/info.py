import pandas as pd

try:
    df = pd.read_csv('dataset.csv')
    df_info = df.info()
    print(df_info)

except Exception as err:
    print(err)
