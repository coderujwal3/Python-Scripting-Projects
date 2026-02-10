# 🌦️ Weather CLI Reporter Script
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

## Example Inputs:
  python weather.py Delhi
  python weather.py "New York"
  python weather.py Prayagraj

## Dependencies:
  pip install requests geopy

## Author:
  Ujwal Singh

## Output Look
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
# Location CLI Report Script
-----------------------------------------
A Python command-line utility that fetches
address, latitude, longitude as well as some
raw dataset like - place id, license, and lot more.

## Data Source:
- geopy.geoencoders (Nominatim)

## Features:
✔ Accepting the Place name (with spaces)
✔ Using those place names to identify the details
✔ Print the details like address, latitude, longitude and som raw data

## Usage:
  python location.py <place_name>

## Example Inputs:
  python weather.py civil lines prayagraj
  python weather.py blw varanasi
  python weather.py delhi

## Dependencies:
  pip install geopy

## Author:
  Ujwal Singh

## Output Look
```
----------> Usage: python location.py <Place_name>

Location Report of 'Blw varanasi'
-------------------------------------------------------
| Address:   | Banaras Locomotive Works, DLW Colony, Varanasi, Uttar Pradesh, India
| Latitude:  | 25.2620
| Longitude: | 82.9793
------------------------------
| Raw Data:
{
  ....
  ....
}
-------------------------------------------------------
```
