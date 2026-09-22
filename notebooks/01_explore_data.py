import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/solar_data.csv")

print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.scatter(df["solar_irradiance"], df["power_output"])
plt.xlabel("Solar Irradiance")
plt.ylabel("Power Output")
plt.title("Solar Irradiance vs Power Output")
plt.grid(True)
plt.show()
plt.savefig("data/solar_irradiance_vs_power.png")
# Correlation analysis

print("\nCorrelation with Power Output:")
print(df.corr(numeric_only=True)["power_output"].sort_values(ascending=False))