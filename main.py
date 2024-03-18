import requests
import json

url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

querystring = {"lat":"35.5","lon":"-78.5"}

headers = {
	"X-RapidAPI-Key": "4e50b14185msh01ad6d45b3f780fp1b0324jsn37cdfa6d2a57",
	"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

response_json = json.loads(response.text)

tempCelsius = (response_json['data'][0]['temp']) #due to the json having multi layers,  we need the [0] index to grab values that are in the list object.
tempFarenheit = round((tempCelsius * 9/5) + 32)

print(tempFarenheit)