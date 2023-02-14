import pandas as pd

try:
    df = pd.read_json('dataset.json')
    print(df)

except Exception as err:
    print(err)
