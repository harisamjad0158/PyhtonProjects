
# API KEY # c2af4f2b82069ad85d01e46a014197d9


import requests
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] == "404":
        return None
    else:
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather_info

def main():
    city = input("Enter the city name: ")
    api_key = input("Enter the API key: ")

    weather_info = get_weather(city, api_key)

    if weather_info:
        print(f"\nWeather in {weather_info['city']}:")
        print(f"Temperature: {weather_info['temperature']} °C")
        print(f"Description: {weather_info['description']}")
        print(f"Humidity: {weather_info['humidity']}%")
        print(f"Wind Speed: {weather_info['wind_speed']} m/s")
    else:
        print("City not found or invalid API key.")

if __name__ == "__main__":
    main()
