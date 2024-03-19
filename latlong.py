import requests
import json
import urllib.parse

# address = 'Durham, North Carolina, NC, 27703'
# osmURL = 'https://nominatim.openstreetmap.org/search?q=' + urllib.parse.quote(address) + '&format=json'
# osmURLresponse = requests.get(osmURL)

# try:
#     osmURLresponse_json = osmURLresponse.json()
#     print(osmURLresponse_json[0]["lat"])
#     print(osmURLresponse_json[0]["lon"])
# except (json.JSONDecodeError, IndexError):
#     print("Error: Unable to retrieve latitude and longitude from OpenStreetMap API.")




data = [
    {"state": "MD", "city": "Baltimore", "country": "usa"},
    {"state": "MI", "city": "Highland", "country": "usa"},
    {"state": "SC", "city": "Sumter", "country": "usa"}
]

results = []

for row in data:
    # Remove parentheses and state abbreviation (if present) from the city name
    city = (row['city']).split("(")[0].strip().rstrip(", MA") # example MA
    state = (row['state']).split("(")[0].strip()
    country = (row['country']).split("()")[0].strip()

    url = f"https://nominatim.openstreetmap.org/search.php?city={city}&state={state}&country={country}&format=jsonv2&addressdetails=1&limit=1"
    response = requests.get(url)
    
    try:
        data = response.json()
        if data:
            # Extract the latitude and longitude from the first result
            lat = float(data[0]["lat"])
            lon = float(data[0]["lon"])
            # Add the city, latitude, and longitude to the results list
            results.append({"city": city, "lat": lat, "lon": lon})
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON response for {city}, {state}, {country}")
        print(f"Response content: {response.content}")
    except KeyError:
        print(f"Error: Latitude or longitude not found in response for {city}, {state}, {country}")

print(results)
