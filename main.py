import requests
import json
import urllib.parse

url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

# address = 'Durham, North Carolina, NC, 27703'
# osmURL = 'https://nominatim.openstreetmap.org/search?q=' + urllib.parse.quote(address) + '&format=json'
# osmURLresponse = requests.get(osmURL)
# osmURLresponse_json = json.loads(osmURLresponse.text)
# print(osmURLresponse_json[0]["lat"])
# print(osmURLresponse_json[0]["lon"])


querystring = {"lat":"35.5","lon":"-78.5"}

headers = {
	"X-RapidAPI-Key": "4e50b14185msh01ad6d45b3f780fp1b0324jsn37cdfa6d2a57",
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




