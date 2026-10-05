import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("supermarket_sales.csv")

# First look
print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- DATA INFO ---")
print(df.info())

print("\n--- DATA SHAPE ---")
print(df.shape)

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())