import sqlite3
import pandas as pd

try:
    db_connection = sqlite3.connect("dataset.db")
    df = pd.read_sql(
        'SELECT * FROM classroom', db_connection)

    print(df)

except Exception as err:
    print(err)
