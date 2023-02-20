import pandas as pd

try:
    df = pd.read_csv('dataset.csv')
    print(df.memory_usage())

except Exception as err:
    print(err)
