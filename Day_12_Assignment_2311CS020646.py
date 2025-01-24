# Day_12_Assignment
import pandas as pd
import matplotlib.pyplot as plt

file_path = "/content/drive/MyDrive/Day_12_banking_data.csv"
df = pd.read_csv(file_path)
transaction_sum = df.groupby('Account_Type')['Transaction_Amount'].sum()
plt.figure(figsize=(10, 6))
transaction_sum.plot(kind='bar', color='skyblue')
plt.title('Total Sum of Transaction Amount per Account Type')
plt.xlabel('Account Type')
plt.ylabel('Total Transaction Amount')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
# Task 2
branch_counts = df['Branch'].value_counts()
plt.figure(figsize=(8, 8))
branch_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Percentage of Transactions per Branch')
plt.ylabel('')
plt.show()