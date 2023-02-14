import pandas as pd

try:
    li = pd.read_html("dataset.html", match="Hassan")
    print(li)

except Exception as err:
    print(err)
