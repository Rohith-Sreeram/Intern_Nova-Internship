import pandas as pd

data = {
    "Name": ["Ravi", "Priya", "Arun", "Sneha", "Kiran"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88],
    "Department": ["CSE", "ECE", "CSE", "ECE", "CSE"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nSelected Columns:")
print(df[["Name", "Marks"]])

print("\nSelected Rows:")
print(df.iloc[0:3])

print("\nMarks Greater Than 85:")
print(df[df["Marks"] > 85])

print("\nMultiple Conditions:")
print(df[(df["Marks"] > 85) & (df["Department"] == "ECE")])

print("\nAscending Order:")
print(df.sort_values(by="Marks"))

print("\nDescending Order:")
print(df.sort_values(by="Marks", ascending=False))