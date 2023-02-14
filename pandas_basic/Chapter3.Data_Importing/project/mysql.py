import mysql.connector as sql
import pandas as pd

db_connection = sql.connect(
    host='127.0.0.1', database='mock', user='arash', password='xx123456')

db_cursor = db_connection.cursor()
db_cursor.execute('SELECT * FROM classroom')

table_rows = db_cursor.fetchall()
df = pd.DataFrame(table_rows)

print(df)
