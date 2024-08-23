import requests
import pandas as pd
import json
import csv

#Access weather API and pass in geographic coordinates
URL = 'https://api.weather.gov/points/32.85,-96.86'
#URL = 'https://api.weather.gov/gridpoints/FWD/87,107/forecast/hourly'

#Send the API request
response = requests.get(URL)

#Store weather data
weather_data = response.json()

#print(response.json())

# Save text of the data to a CSV file
with open("weather.csv", "a") as csv:
    csv.write(response.text)