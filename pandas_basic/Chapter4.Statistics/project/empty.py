import pandas as pd

try:
    df = pd.DataFrame({
        'Name': []
    })
    print(df.info())
    print(df.empty)

except Exception as err:
    print(err)
