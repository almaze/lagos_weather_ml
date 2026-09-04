import pandas as pd
from pathlib import Path


RAW_DATA_PATH = (
    Path(__file__).parent.parent
    / "data"
    / "raw"
    / "lagos_weather_raw.csv"
)


df = pd.read_csv(RAW_DATA_PATH)

print("===== DATASET SHAPE =====")
print(df.shape)

print("\n===== COLUMNS =====")
print(df.columns.tolist())

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

print("\n===== SUMMARY STATISTICS =====")
print(df.describe())