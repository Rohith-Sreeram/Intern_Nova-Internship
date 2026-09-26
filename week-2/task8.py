import pandas as pd

students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Ravi", "Priya", "Arun", "Sneha", "Kiran"],
    "Department": ["CSE", "ECE", "CSE", "ECE", "CSE"]
})

marks = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105],
    "Marks": [85, 90, 78, 92, 88],
    "Attendance": [90, 95, 85, 98, 92]
})

print("Students DataFrame:")
print(students)

print("\nMarks DataFrame:")
print(marks)

merged_df = pd.merge(students, marks, on="Student_ID")

print("\nMerged DataFrame:")
print(merged_df)

data1 = pd.DataFrame({
    "Student_ID": [106, 107],
    "Name": ["Anil", "Divya"],
    "Department": ["ECE", "CSE"]
})

concatenated_df = pd.concat([students, data1], ignore_index=True)

print("\nConcatenated DataFrame:")
print(concatenated_df)

grouped = merged_df.groupby("Department")["Marks"].agg(
    ["sum", "mean", "count", "min", "max"]
)

print("\nGroupBy Results:")
print(grouped)

pivot_table = pd.pivot_table(
    merged_df,
    values="Marks",
    index="Department",
    columns="Attendance",
    aggfunc="mean"
)

print("\nPivot Table:")
print(pivot_table)