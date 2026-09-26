import pandas as pd

data = {
    "Name": ["Ravi", "Priya", "Arun", "Sneha", "Kiran"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88],
    "Department": ["CSE", "ECE", "CSE", "ECE", "CSE"]
}

df = pd.DataFrame(data)

df["Result"] = ["Pass", "Pass", "Pass", "Pass", "Pass"]

file_name = "processed_students.csv"

df.to_csv(file_name, index=False)

print("Processed DataFrame:")
print(df)

exported_df = pd.read_csv(file_name)

print("\nExported CSV Data:")
print(exported_df)

print("\nFile exported successfully:", file_name)