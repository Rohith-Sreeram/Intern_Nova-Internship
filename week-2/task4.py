import pandas as pd

series = pd.Series([85, 90, 78, 92, 88])

print("Pandas Series:")
print(series)

data = {
    "Name": ["Ravi", "Priya", "Arun", "Sneha", "Kiran"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

print("\nColumn Names:")
print(df.columns)

print("\nIndex:")
print(df.index)

df["Grade"] = ["A", "A+", "B", "A+", "A"]

print("\nUpdated DataFrame:")
print(df)