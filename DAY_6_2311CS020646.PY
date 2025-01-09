import pandas as pd
data = {"Name": ["John", "Alice", "Bob", "Diana"],"Age": [28, 34, 23, 29],"Department": ["HR", "IT", "Marketing", "Finance"],"Salary": [45000, 60000, 35000, 50000]}
df = pd.DataFrame(data)
print("First 2 rows:")
print(df.head(2))
df["Bonus"] = df["Salary"] * 0.10
print("DataFrame with Bonus column:")
print(df)
average_salary = df["Salary"].mean()
print("Average Salary:", average_salary)
filtered_df = df[df["Age"] > 25]
print("Employees older than 25:")
print(filtered_df)
