import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    "timestamp": pd.date_range(start="2025-01-01", periods=100, freq="h"),
    "solar_irradiance": np.random.uniform(0, 1000, 100),
    "temperature": np.random.uniform(15, 45, 100),
    "humidity": np.random.uniform(20, 90, 100),
    "wind_speed": np.random.uniform(0, 15, 100),
    "power_output": np.random.uniform(0, 500, 100)
}

df = pd.DataFrame(data)

df.to_csv("data/solar_data.csv", index=False)

print("Solar dataset created successfully!")
print(df.head())