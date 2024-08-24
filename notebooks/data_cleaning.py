import pandas as pd
file_path = 'data/benin-malanville.csv'
df = pd.read_csv(file_path)
print("First few rows of the DataFrame:")
print(df.head())  
print("\nDataFrame info:")
print(df.info()) 
print("\nSummary statistics:")
print(df.describe(include='all'))
print("\nMissing values per column:")
print(df.isna().sum())
