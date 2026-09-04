import pandas as pd
from pathlib import Path
import datetime


RAW_DATA_PATH = (
    Path(__file__).parent.parent
    / "data"
    / "raw"
    / "lagos_weather_raw.csv"
)

PROCESSED_DATA_PATH = (
    Path(__file__).parent.parent
    / "data"
    / "processed"
    / "lagos_weather_transformed.csv"
)


def transform_weather_data(df):
    # Rename API field to our preferred name
    df = df.rename(columns={"time": "date"})

    # Convert date to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Sort chronologically
    df = df.sort_values("date").reset_index(drop=True)

    return df


if __name__ == "__main__":

    # Read raw data
    df = pd.read_csv(RAW_DATA_PATH)


    # Transform data
    df = transform_weather_data(df)


    # Save transformed data
    df.to_csv(PROCESSED_DATA_PATH, index=False)

    print("Transformation completed.")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print(f"Saved to: {PROCESSED_DATA_PATH}")