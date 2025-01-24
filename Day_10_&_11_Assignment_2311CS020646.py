#Day_10_&_11_Assignment
import pandas as pd

file_path = "/content/drive/MyDrive/Day_10_banking_data.csv"
df = pd.read_csv(file_path)
print("First 5 rows of the dataset:")
print(df.head())


#Assignment-1
filtered_amount = df[df['Transaction_Amount'] <= 2000]
print("\nFiltered by Transaction Amount > 2000:")
print(filtered_amount)
filtered_loan_payment = df[(df['Transaction_Type'] == 'Loan Payment') & (df['Account_Balance'] > 5000)]
print("\nFiltered Loan Payments with Account Balance > 5000:")
print(filtered_loan_payment)
filtered_uptown = df[df['Branch'] == 'Uptown']
print("\nTransactions made in the Uptown branch:")
print(filtered_uptown)


#Assignment-2
df['Transaction_Fee'] = df['Transaction_Amount'] * 0.02
print("\nDataFrame with Transaction Fee:")
print(df)
df['Balance_Status'] = df['Account_Balance'].apply(lambda x: 'High Balance' if x > 5000 else 'Low Balance')
print("\nDataFrame with Balance Status:")
print(df)