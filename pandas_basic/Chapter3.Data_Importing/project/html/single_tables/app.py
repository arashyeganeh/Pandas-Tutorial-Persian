import pandas as pd

try:
    li = pd.read_html("dataset.html")
    print(li)
    print(type(li))

except Exception as err:
    print(err)
