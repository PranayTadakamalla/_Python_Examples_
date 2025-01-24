#Day_14_Assignment
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "/content/drive/MyDrive/Day_14_Pharma_data.csv"
data = pd.read_csv(file_path)

# Displaying the first few rows of the dataset
print(data.head())
# Data Cleaning
# Check for missing values we use here isnull()
print(data.isnull().sum())
duplicates = data.duplicated().sum()
print(f'Duplicates: {duplicates}')

# Remove duplicates if any
data = data.drop_duplicates()

# Visualizations
# 1. Bar plot comparing the average Effectiveness for each drug across different regions
plt.figure(figsize=(12, 6))
sns.barplot(x='Product_Name', y='Effectiveness', hue='Region', data=data, estimator='mean')
plt.title('Average Effectiveness for Each Drug across Different Regions')
plt.xlabel('Drug')
plt.ylabel('Average Effectiveness')
plt.xticks(rotation=45)
plt.legend(title='Region')
plt.show()
# 2. Violin plot to show the distribution of Effectiveness and Side_Effects for each product
plt.figure(figsize=(12, 6))
sns.violinplot(x='Product_Name', y='Effectiveness', data=data, inner='quartile')
plt.title('Distribution of Effectiveness for Each Product')
plt.xlabel('Product')
plt.ylabel('Effectiveness')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.violinplot(x='Product_Name', y='Side_Effects', data=data, inner='quartile')
plt.title('Distribution of Side Effects for Each Product')
plt.xlabel('Product')
plt.ylabel('Side Effects')
plt.xticks(rotation=45)
plt.show()
# 3. Pairplot to explore relationships between Effectiveness, Side_Effects, and Marketing_Spend
sns.pairplot(data[['Effectiveness', 'Side_Effects', 'Marketing_Spend']])
plt.suptitle('Pairplot of Effectiveness, Side Effects, and Marketing Spend', y=1.02)
plt.show()
# 4. Boxplot comparing Effectiveness for different trial periods
plt.figure(figsize=(12, 6))
sns.boxplot(x='Trial_Period', y='Effectiveness', data=data)
plt.title('Effectiveness for Different Trial Periods')
plt.xlabel('Trial Period')
plt.ylabel('Effectiveness')
plt.xticks(rotation=45)
plt.show()

# 5. Regression plot to analyze how Marketing_Spend affects drug Effectiveness
plt.figure(figsize=(10, 6))
sns.regplot(x='Marketing_Spend', y='Effectiveness', data=data)
plt.title('Effect of Marketing Spend on Drug Effectiveness')
plt.xlabel('Marketing Spend')
plt.ylabel('Effectiveness')
plt.show()