import pandas as pd

dataSet = {
    "Name": [
        "Arash",
        "Shahram",
        "Omid",
        "Morteza",
        "Najme",
        "Mahsa",
        "Elham",
        "Maryam",
        "Sanam",
    ],
    "Physic ": [15, 15.25, 18, 17, 8, 14, 18, 17, 13],
    "chemistry": [16, 16, 10, 9, 15, 19, 16.25, 12.5, 19],
    "mathematic": [14, 10, 15, 12, 13, 15.75, 16, 19, 14],
}

df = pd.DataFrame(dataSet)
df = df.sort_values(
    by=["Name"]
)  # you can use "inplace=True" Instead of reassign to variable in argument.
print(df)
