import pandas as pd
import numpy as np

data = {
    "Name": ["Ravi", "Priya", "Arun", "Sneha", "Kiran"],
    "Age": [20, 21, np.nan, 22, 20],
    "Marks": [85, np.nan, 78, 92, 88],
    "Department": ["CSE", "ECE", "CSE", np.nan, "CSE"]
}

df = pd.DataFrame(data)

print("Dataset Before Handling Missing Values:")
print(df)

print("\nMissing Values:")
print(df.isnull())

print("\nMissing Values in Each Column:")
print(df.isna().sum())

removed_df = df.dropna()

print("\nDataset After Removing Rows With Missing Values:")
print(removed_df)

filled_df = df.copy()

filled_df["Age"] = filled_df["Age"].fillna(filled_df["Age"].mean())
filled_df["Marks"] = filled_df["Marks"].fillna(filled_df["Marks"].mean())
filled_df["Department"] = filled_df["Department"].fillna("Unknown")

print("\nDataset After Filling Missing Values:")
print(filled_df)