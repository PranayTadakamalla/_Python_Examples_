#Day_13_Assignment
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = "/content/drive/MyDrive/Day_13_Pharma_data.csv"
data = pd.read_csv(file_path)
# Display the first few rows of the dataset
print(data.head())

# Data Cleaning
# Check for missing values
print(data.isnull().sum())

# Check for duplicates
duplicates = data.duplicated().sum()
print(f'Duplicates: {duplicates}')
data = data.drop_duplicates()
#1
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Sales', data=data, estimator=sum)
plt.title('Total Sales per Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()
#2
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Marketing_Spend', y='Sales', data=data)
plt.title('Relationship between Marketing Spend and Sales')
plt.xlabel('Marketing Spend')
plt.ylabel('Sales')
plt.show()
#3
plt.figure(figsize=(10, 6))
sns.boxplot(x='Age_Group', y='Effectiveness', data=data)
plt.title('Drug Effectiveness across Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Effectiveness')
plt.xticks(rotation=45)
plt.show()
#4
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='Trial_Period', y='Sales', hue='Product_Name', marker='o')
plt.title('Sales Trend for Each Product over Trial Periods')
plt.xlabel('Trial Period')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.legend(title='Product')
plt.show()
#5
correlation_matrix = data[['Sales', 'Marketing_Spend', 'Effectiveness']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()