#Day_9_Assignment
import pandas as pd

file_path = '/content/drive/MyDrive/Day_9_banking_data.csv'
data = pd.read_csv(file_path)
print("First 5 rows of the dataset:")
print(data.head())
print("\nBasic statistics of numerical columns:")
print(data.describe())
print("\nMissing values in the dataset:")
print(data.isnull().sum())

account_group = data.groupby('Account_Type').agg({
    'Transaction_Amount': 'sum',
    'Account_Balance': 'mean'
}).reset_index()
print("\nAggregated data by Account_Type:")
print(account_group)
branch_group = data.groupby('Branch').agg({
    'Transaction_Amount': ['count', 'mean']
}).reset_index()
branch_group.columns = ['Branch', 'Total_Transactions', 'Average_Transaction_Amount']
print("\nAggregated data by Branch:")
print(branch_group)