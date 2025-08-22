import requests


API_KEY = "72ec2ba5feb448436283b37aa395cef7"
CITY = input("Enter the name of your city: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&APPID={API_KEY}")

if weather_data.json()['cod'] == '404':
    print("No city found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    print(f"The weather in {CITY} is: {weather}")
    print(f"the temperature in {CITY} is: {temp}°C")