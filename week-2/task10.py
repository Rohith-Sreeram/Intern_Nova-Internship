import numpy as np
import pandas as pd

data = {
    "Name": ["Ravi", "Priya", "Arun", "Sneha", "Kiran", "Anil", "Divya", "Rahul"],
    "Department": ["CSE", "ECE", "CSE", "ECE", "CSE", "ECE", "CSE", "ECE"],
    "Age": [20, 21, 19, 22, 20, 21, 19, 22],
    "Marks": [85, 90, 78, 92, 88, 75, 95, 82],
    "Attendance": [90, 95, 85, 98, 92, 80, 96, 88]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("\nDataset Information:")
df.info()

print("\nFirst 5 Rows:")
print(df.head())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

print("\nDataset After Handling Missing Values:")
print(df)

print("\nStudents With Marks Greater Than 85:")
print(df[df["Marks"] > 85])

print("\nStudents With Attendance Greater Than 90:")
print(df[df["Attendance"] > 90])

print("\nStudents With Marks Greater Than 85 and Attendance Greater Than 90:")
print(df[(df["Marks"] > 85) & (df["Attendance"] > 90)])

sorted_df = df.sort_values(by="Marks", ascending=False)

print("\nStudents Sorted by Marks:")
print(sorted_df)

grouped = df.groupby("Department")["Marks"].agg(
    ["mean", "sum", "count", "min", "max"]
)

print("\nGroupBy Analysis:")
print(grouped)

pivot = pd.pivot_table(
    df,
    values="Marks",
    index="Department",
    columns="Attendance",
    aggfunc="mean"
)

print("\nPivot Table:")
print(pivot)

marks = np.array(df["Marks"])

print("\nNumPy Analysis:")
print("Mean Marks:", np.mean(marks))
print("Maximum Marks:", np.max(marks))
print("Minimum Marks:", np.min(marks))
print("Standard Deviation:", np.std(marks))

print("\nUseful Insights:")
print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
print("Average Attendance:", df["Attendance"].mean())

df.to_csv("cleaned_student_performance.csv", index=False)

verified_df = pd.read_csv("cleaned_student_performance.csv")

print("\nExported Processed Dataset:")
print(verified_df)

print("\nDataset exported successfully as cleaned_student_performance.csv")