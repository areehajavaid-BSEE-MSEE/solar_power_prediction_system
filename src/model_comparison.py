import pandas as pd

results = pd.DataFrame({
    "Model": ["Random Forest", "Linear Regression"],
    "MAE": [27.260555467029935, 21.119329835647967],
    "MSE": [1244.2000302298707, 821.7077014686558],
    "RMSE": [35.27321973154521, 28.665444379403155],
    "R2": [0.9195019658450818, 0.9468366395988895]
})

print(results)

results.to_csv("data/model_comparison.csv", index=False)

print("\nModel comparison saved successfully!")