import requests, sys

API_KEY = 'f4bff1e98c5c50dea8c76b8c3a9082b2'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

try:
    city = sys.argv[1]
except IndexError:
    city = input('Enter city name: ')

r = requests.get(f'{BASE_URL}?q={city}&appid={API_KEY}&units=metric')

if r.status_code == 200:
    response = r.json()
    description = response['weather'][0]['description']
    temp = response['main']['temp']
    print(description.capitalize())
    print(f'{temp} \N{DEGREE SIGN}C')
else:
    print('Could not retrieve weather data for given city')
    print(f'Error ID: {r.status_code}')