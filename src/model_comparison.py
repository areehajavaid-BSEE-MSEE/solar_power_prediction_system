import pandas as pd
import matplotlib.pyplot as plt

# Load model comparison results
results = pd.read_csv("data/model_comparison.csv")

# Plot R² comparison
plt.figure(figsize=(8, 5))
plt.bar(results["Model"], results["R2"])
plt.ylabel("R² Score")
plt.xlabel("Model")
plt.title("Model Performance Comparison")
plt.ylim(0, 1)
plt.grid(axis="y")

# Save figure
plt.savefig("data/model_performance_comparison.png")

plt.show()