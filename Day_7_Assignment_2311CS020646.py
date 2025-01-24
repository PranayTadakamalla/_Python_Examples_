# Day_7_Assignment

import pandas as pd

file_path = "/content/drive/MyDrive/Day_7_sales_data.csv"
data = pd.read_csv(file_path)

print("First 5 rows of the dataset:")
print(data.head())

print("\nBasic statistics of numerical columns:")
print(data.describe())

total_sales_by_region = data.groupby('Region')['Sales'].sum()

print("\nTotal Sales for Each Region:")
print(total_sales_by_region)

most_sold_product = data.groupby('Product')['Quantity'].sum().idxmax()
most_sold_quantity = data.groupby('Product')['Quantity'].sum().max()

print("\nMost Sold Product:")
print(f"Product: {most_sold_product}, Total Quantity Sold: {most_sold_quantity}")

data['Profit_Margin'] = (data['Profit'] / data['Sales']) * 100
average_profit_margin = data.groupby('Product')['Profit_Margin'].mean()

print("\nAverage Profit Margin for Each Product:")
print(average_profit_margin)
