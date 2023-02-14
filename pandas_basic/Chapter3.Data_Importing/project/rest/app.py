import requests
import json
import pandas as pd

try:
    # Senario 1 👇
    response = requests.get("http://localhost:3000")
    # "http://127.0.0.1:3000" = "http://localhost:3000"

    if response.status_code == 200:
        data_json = response.json()
        data_json = json.dumps(data_json)
        df = pd.read_json(data_json)
        print(df)

    # Senario 2 👇
    # df = pd.read_json("http://localhost:3000")  # Or "http://127.0.0.1:3000"
    # print(df)


except Exception as err:
    print(err)
