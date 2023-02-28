import pandas as pd

data = {
    'point': [999, 90, 99, 104, 105, 94, 99, 104],
    'name': ['A', 'B', 'B', 'B', 'A', 'C', 'D', 'B']
}
df = pd.DataFrame(data)
print(df.groupby(['name']).mean())
