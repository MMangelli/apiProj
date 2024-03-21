import requests
import os
from dotenv import load_dotenv
import json
import urllib.parse
from latlong import get_lat_long

load_dotenv()
api_key = os.getenv("API_KEY")
url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"


#figure out how to reference a separate py file to grab the lat long variables
location = input("Type a Location as City, State \n")
latitude, longitude = get_lat_long(location)

querystring = {"lat": latitude,"lon": longitude}

headers = {
	"X-RapidAPI-Key": api_key,
	"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

response_json = json.loads(response.text)
data = (response_json['data'])

#Grab each value from dictionary
for item in data:
    celsius_temp = item['temp']
    
    #Convert C to F
    fahrenheit_temp = (celsius_temp * 9/5) + 32

    print(f"Celsius: {celsius_temp}, Fahrenheit: {fahrenheit_temp}")




