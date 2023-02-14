import pandas as pd

try:
    li = pd.read_html(
        "https://github.com/arashyeganeh/Pandas-Tutorial-Persian")
    print(li)

except Exception as err:
    print(err)
