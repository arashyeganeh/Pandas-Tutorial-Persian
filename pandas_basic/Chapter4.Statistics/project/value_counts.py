import pandas as pd

try:
    df = pd.read_csv('dataset.csv')
    print(df["Chemistry"].value_counts())

except Exception as err:
    print(err)
