import pandas as pd

try:
    df = pd.read_excel('dataset.xlsx')
    print(df)

except Exception as err:
    print(err)
