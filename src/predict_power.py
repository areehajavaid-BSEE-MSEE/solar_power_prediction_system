import pandas as pd
import joblib

# Load trained model
model = joblib.load("src/solar_power_model.pkl")

# Example conditions
new_data = pd.DataFrame({
    "solar_irradiance": [800],
    "temperature": [30],
    "humidity": [50],
    "wind_speed": [5]
})

# Predict power output
prediction = model.predict(new_data)

print("Predicted Solar Power Output:", prediction[0])
result = new_data.copy()
result["predicted_power_output"] = prediction

result.to_csv("data/prediction_result.csv", index=False)

print("Prediction result saved successfully!")