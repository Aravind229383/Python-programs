import json
with open('weather_data.json')as f:
    data=json.load(f)
current_temp=dtaa['main']['temp']
humidity=data['main']['humidity']
weather_desc=data['weather'][0]['description']
print(f"current temperature: {current_temp}c")
print(f"humidity: {humidity}%")
print(f"weather description: {weather_desc}")