# Script to get any locations weather report (requires parameter as a place name (like - delhi, prayagraj, Uttar Pradesh, or Washington))
import sys
import requests
from datetime import datetime
from geopy import Nominatim

def iso_to_time(ts):
    return datetime.fromisoformat(ts).strftime("%H:%M:%S")

def main():
    if len(sys.argv) != 2:
        print("\nPython weather.py <API_KEY> <CITY_ID> is not working, use the <PLACE> parameter instead")
        print("Usage: python weather.py <Place_name>\n")          # <--- how to run this program
        sys.exit(1)

    city = sys.argv[1]

    # extracting the latitude and longitude of the given location, because this geopy accepts lat & lon as parameters
    get_loc = Nominatim(user_agent="GetLoc")
    location = get_loc.geocode(city)

    if not location:
        print("Location not found")
        sys.exit(1)

    lat = location.latitude
    lon = location.longitude

    # API endpoint used to extract data
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "surface_pressure",
            "wind_speed_10m",
            "cloud_cover"
        ],
        "daily": [
            "temperature_2m_min",
            "temperature_2m_max",
            "sunrise",
            "sunset"
        ],
        "timezone": "auto"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error fetching weather data")
        sys.exit(1)

    data = response.json()
    
    print("\033c\033[3J", end='')
    print(f"\n🌍 Weather Report of {city}")
    print("-" * 35)
    print(f"Temperature    : Min {data['daily']['temperature_2m_min'][0]}°C || "
          f"Max {data['daily']['temperature_2m_max'][0]}°C")
    print(f"Humidity       : {data['current']['relative_humidity_2m']}%")
    print(f"Pressure       : {data['current']['surface_pressure']} hPa")
    print(f"Wind Speed     : {data['current']['wind_speed_10m']} m/s")
    print(f"Cloud Cover    : {data['current']['cloud_cover']}%")
    print(f"Sunrise        : {iso_to_time(data['daily']['sunrise'][0])}")
    print(f"Sunset         : {iso_to_time(data['daily']['sunset'][0])}")
    print(f"Latitude       : {lat}")
    print(f"Longitude      : {lon}")
    print("-" * 35)

if __name__ == "__main__":
    main()