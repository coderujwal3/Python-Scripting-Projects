import sys
import json
from geopy.geocoders import Nominatim

def main():
    # how to use this script
    print("----------> Usage: python location.py <Place_name>")

    appName = Nominatim(user_agent="getloc")
    inp_loc = sys.argv[1:]
    location = appName.geocode(inp_loc)
    report_of = ' '.join(inp_loc)
    print(f"\nLocation Report of '{report_of.capitalize()}'")
    print("-"*55)
    print(f"| Address:   | {location.address}")
    print(f"| Latitude:  | {location.latitude}")
    print(f"| Longitude: | {location.longitude}")
    print("-"*30)
    print("| Raw Data:")
    print(json.dumps(location.raw, indent=2))
    print("-"*55)

if __name__ == "__main__":
    main()