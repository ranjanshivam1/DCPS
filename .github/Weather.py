import requests

def get_weather(api_key, city):
    # Weatherbit API endpoint URL
    url = f"https://api.weatherbit.io/v2.0/current?city={city}&key={api_key}"

    try:
        # Make GET request to Weatherbit API
        response = requests.get(url)
        
        # Check if request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON response
            weather_data = response.json()
            # Extract relevant weather information
            temperature = weather_data['data'][0]['temp']
            weather_description = weather_data['data'][0]['weather']['description']
            humidity = weather_data['data'][0]['rh']
            wind_speed = weather_data['data'][0]['wind_spd']
            # Return weather data
            return temperature, weather_description, humidity, wind_speed
        else:
            # Print error message if request was unsuccessful
            print(f"Error: Unable to retrieve weather data. Status code: {response.status_code}")
            return None
    except Exception as e:
        # Print error message if an exception occurs
        print(f"An error occurred: {str(e)}")
        return None

# Replace 'YOUR_API_KEY' with your actual Weatherbit API key
api_key = 'bc587fb4640b4467a708a3ef73d2ab79'
# Specify the city for which you want to retrieve weather data (e.g., Mumbai)
city = 'Mumbai'

# Call the get_weather function to retrieve weather data
weather_data = get_weather(api_key, city)
if weather_data:
    temperature, weather_description, humidity, wind_speed = weather_data
    print(f"Current weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Weather Description: {weather_description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
