import requests
import pandas as pd
from pathlib import Path

from confg import LATITUDE, LONGITUDE, DAILY_PARAMETERS, START_DATE, END_DATE

RAW_DATA_PATH = Path(__file__).parent.parent / "data" / "raw" / "lagos_weather_raw.csv"

def extract_weather_data(start_date, end_date):
    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "start_date": start_date,
        "end_date": end_date,
        "daily": ",".join(DAILY_PARAMETERS),
        "timezone": "auto",
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame(data["daily"])

    return df


if __name__ == "__main__":
    df = extract_weather_data(
        start_date=START_DATE,
        end_date=END_DATE
    )

    df.to_csv(RAW_DATA_PATH, index=False)

    print(df.head())
    print()
    print(df.tail())
    print()
    print(f"Rows: {len(df)}")
    print(f"Saved to: {RAW_DATA_PATH}")