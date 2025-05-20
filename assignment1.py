import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Configuration
LATITUDE = 51.5074  # London coordinates
LONGITUDE = -0.1278
BASE_URL = "https://api.open-meteo.com/v1/forecast"

# Function to fetch weather forecast
def get_forecast(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,relative_humidity_2m,precipitation_probability,weather_code",
        "forecast_days": 5
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching forecast: {response.status_code}")

# Fetch data
try:
    forecast_data = get_forecast(LATITUDE, LONGITUDE)
except Exception as e:
    print(e)
    exit()

# Process forecast data
hourly = forecast_data["hourly"]
forecast_df = pd.DataFrame({
    "time": pd.to_datetime(hourly["time"]),
    "temp": hourly["temperature_2m"],
    "humidity": hourly["relative_humidity_2m"],
    "precip_prob": hourly["precipitation_probability"],
    "weather_code": hourly["weather_code"]
})

# Map weather codes to descriptions (simplified)
weather_map = {
    0: "Clear", 1: "Mainly Clear", 2: "Partly Cloudy", 3: "Overcast",
    51: "Light Drizzle", 61: "Light Rain", 63: "Moderate Rain", 80: "Rain Showers"
}
forecast_df["weather"] = forecast_df["weather_code"].map(lambda x: weather_map.get(x, "Other"))

# Set up the visualization style
sns.set_style("whitegrid")

# Plot 1: Temperature over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=forecast_df, x="time", y="temp", marker="o")
plt.title("Temperature Forecast for London")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temperature_forecast.png")
plt.close()

# Plot 2: Weather conditions frequency
plt.figure(figsize=(10, 6))
weather_counts = forecast_df["weather"].value_counts()
sns.barplot(x=weather_counts.index, y=weather_counts.values)
plt.title("Weather Conditions Frequency")
plt.xlabel("Weather Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("weather_conditions.png")
plt.close()

# Plot 3: Temperature vs Humidity
plt.figure(figsize=(10, 6))
sns.scatterplot(data=forecast_df, x="temp", y="humidity", hue="weather", size="precip_prob")
plt.title("Temperature vs Humidity")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.tight_layout()
plt.savefig("temp_vs_humidity.png")
plt.close()

# Save current weather summary as text file
current = forecast_df.iloc[0]
summary = (f"Current Weather in London\n"
           f"Temp: {current['temp']}°C\n"
           f"Condition: {current['weather']}\n"
           f"Humidity: {current['humidity']}%")
with open("current_weather.txt", "w") as f:
    f.write(summary)
