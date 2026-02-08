# 🌦️ Weather CLI Reporter
-----------------------------------------
A Python command-line utility that fetches
real-time weather information for any place
in the world using latitude & longitude.

## Data Source:
- Open-Meteo API (weather forecast)
- OpenStreetMap Nominatim (geocoding)

## Features:
✔ Convert place name → coordinates
✔ Current weather conditions
✔ Daily min/max temperature
✔ Sunrise & sunset time
✔ Wind, humidity, pressure, cloud cover
✔ Automatic timezone detection

## Usage:
  python weather.py <place_name>

## Example:
  python weather.py Delhi
  python weather.py "New York"
  python weather.py Prayagraj

## Dependencies:
  pip install requests geopy

## Author:
  Ujwal Singh

# Output Look
```
🌍 Weather Report – Delhi
━━━━━━━━━━━━━━━━━━━━━━━━━━
🌡 Temperature : 18°C (min) / 26°C (max)
💧 Humidity    : 72%
🌬 Wind Speed  : 3.4 m/s
☁ Cloud Cover : 40%
🌅 Sunrise     : 06:54:12
🌇 Sunset      : 17:41:03
📍 Lat, Lon    : 28.61, 77.20
━━━━━━━━━━━━━━━━━━━━━━━━━━
```
