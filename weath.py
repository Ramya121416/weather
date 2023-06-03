import requests
import json
import sys

def getweather(cityname):
    apikey = "ce06988771463bc429148e4e710b75be"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={apikey}"

    try:
        responses = requests.get(url)
        responses.raiseforstatus()
        data = responses.json()

        # Parse the weather data
        weatherdescription = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        # Print the weather forecast
        print(f"Weather forecast for {cityname}:")
        print(f"Description: {weatherdescription}")
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
    except (KeyError, IndexError):
        print("Invalid response received from the API.")
    except json.JSONDecodeError:
        print("Failed to parse the response as JSON.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a city name.")
    else:
        city_name = " ".join(sys.argv[1:])
        get_weather(cityname)
