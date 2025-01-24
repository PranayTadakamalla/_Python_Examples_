#Day_8 Assignment

import pandas as pd

file_path = '/content/drive/MyDrive/Day_8_sales_data.csv'
data = pd.read_csv(file_path)

print("First 5 rows of the dataset:")
print(data.head())
sales_above_1000 = data[data['Sales'] > 1000]
print("\nRows where Sales > 1000:")
print(sales_above_1000)

sales_east_region = data[data['Region'] == "East"]
print("\nSales records for the 'East' region:")
print(sales_east_region)

data['Profit_Per_Unit'] = data['Profit'] / data['Quantity']
print("\nDataset with 'Profit_Per_Unit' column added:")
print(data.head())
data['High_Sales'] = data['Sales'].apply(lambda x: 'Yes' if x > 1000 else 'No')
print("\nDataset with 'High_Sales' column added:")
print(data.head())
