import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

data = {
    'age': [25, 30, 35, 40, 45],
    'height': [150, 160, 170, 180, 190],
    'weight': [50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)
print("Original Dataset:")
print(df)

scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(df)

normalized_df = pd.DataFrame(scaled_data, columns=df.columns)
print("\nNormalized Dataset(scaled to range [0,1]):")
print(normalized_df)
print("\nFeature-wise Min values After Scaling:")
print(normalized_df.min())

scaler = StandardScaler()
standardized_data = scaler.fit_transform(df)

standardized_df = pd.DataFrame(standardized_data, columns=df.columns)

print("Original Dataset:")
print(df)

print("\nNormalized Dataset (scaled to range [0, 1]):")
print(normalized_df)

print("\nStandardized Dataset (mean=0, std=1):")
print(standardized_df)

print("\nFeature-wise Mean values After Standardization:")
print(standardized_df.mean())

print("\nFeature-wise Std values After Standardization:")
print(standardized_df.std())