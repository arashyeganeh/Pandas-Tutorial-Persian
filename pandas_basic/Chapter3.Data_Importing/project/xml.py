import pandas as pd

try:
    df = pd.read_xml("dataset.xml")
    print(df)

except Exception as err:
    print(err)
