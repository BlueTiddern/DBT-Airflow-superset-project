
import requests
from dotenv import load_dotenv
import os

# Load the environment variables and the API key as the secret

load_dotenv()
#api_key = os.getenv("WEATHERSTACK_KEY")
api_key = '0cb3c7495baee731c089402b9e4a3db4'

#Load the api url
api_url = f"https://api.weatherstack.com/current?access_key={api_key}&query=Miamisburg"

# Note: This has been commented out and a function with mock data is added to minimize the number of the api calls
# Uncomment and refactor when using the DAG

def fetch_data():
    print("Fetching weather data...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received successfully")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request Exception Occurred : {e}")
        raise

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'Miamisburg, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Miamisburg', 'country': 'United States of America', 'region': 'Ohio', 'lat': '39.643', 'lon': '-84.287', 'timezone_id': 'America/New_York', 'localtime': '2025-10-02 17:27', 'localtime_epoch': 1759426020, 'utc_offset': '-4.0'}, 'current': {'observation_time': '09:27 PM', 'temperature': 27, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Sunny'], 'astro': {'sunrise': '07:35 AM', 'sunset': '07:17 PM', 'moonrise': '05:07 PM', 'moonset': '02:07 AM', 'moon_phase': 'Waxing Gibbous', 'moon_illumination': 70}, 'air_quality': {'co': '281.85', 'no2': '27.55', 'o3': '83', 'so2': '12.85', 'pm2_5': '21.75', 'pm10': '21.85', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 4, 'wind_degree': 65, 'wind_dir': 'ENE', 'pressure': 1024, 'precip': 0, 'humidity': 33, 'cloudcover': 0, 'feelslike': 25, 'uv_index': 2, 'visibility': 16, 'is_day': 'yes'}}