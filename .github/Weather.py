{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "2aa6af20-70e4-47dc-8d89-5aa17c75123f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Current weather in Mumbai:\n",
      "Temperature: 26°C\n",
      "Weather Description: Smoke\n",
      "Humidity: 50%\n",
      "Wind Speed: 1.5 m/s\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "def get_weather(api_key, city):\n",
    "    # Weatherbit API endpoint URL\n",
    "    url = f\"https://api.weatherbit.io/v2.0/current?city={city}&key={api_key}\"\n",
    "\n",
    "    try:\n",
    "        # Make GET request to Weatherbit API\n",
    "        response = requests.get(url)\n",
    "        \n",
    "        # Check if request was successful (status code 200)\n",
    "        if response.status_code == 200:\n",
    "            # Parse JSON response\n",
    "            weather_data = response.json()\n",
    "            # Extract relevant weather information\n",
    "            temperature = weather_data['data'][0]['temp']\n",
    "            weather_description = weather_data['data'][0]['weather']['description']\n",
    "            humidity = weather_data['data'][0]['rh']\n",
    "            wind_speed = weather_data['data'][0]['wind_spd']\n",
    "            # Return weather data\n",
    "            return temperature, weather_description, humidity, wind_speed\n",
    "        else:\n",
    "            # Print error message if request was unsuccessful\n",
    "            print(f\"Error: Unable to retrieve weather data. Status code: {response.status_code}\")\n",
    "            return None\n",
    "    except Exception as e:\n",
    "        # Print error message if an exception occurs\n",
    "        print(f\"An error occurred: {str(e)}\")\n",
    "        return None\n",
    "\n",
    "# Replace 'YOUR_API_KEY' with your actual Weatherbit API key\n",
    "api_key = 'bc587fb4640b4467a708a3ef73d2ab79'\n",
    "# Specify the city for which you want to retrieve weather data (e.g., Mumbai)\n",
    "city = 'Mumbai'\n",
    "\n",
    "# Call the get_weather function to retrieve weather data\n",
    "weather_data = get_weather(api_key, city)\n",
    "if weather_data:\n",
    "    temperature, weather_description, humidity, wind_speed = weather_data\n",
    "    print(f\"Current weather in {city}:\")\n",
    "    print(f\"Temperature: {temperature}°C\")\n",
    "    print(f\"Weather Description: {weather_description}\")\n",
    "    print(f\"Humidity: {humidity}%\")\n",
    "    print(f\"Wind Speed: {wind_speed} m/s\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60835a66-23bc-498e-a4f1-f6dfcd9de156",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
