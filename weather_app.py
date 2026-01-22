import requests

def get_weather(city_name):
    api_key = "YOUR_API_KEY"   # Replace with your API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        print("\nWeather Details")
        print("---------------------")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Pressure:", data["main"]["pressure"], "hPa")
        print("Wind Speed:", data["wind"]["speed"], "m/s")
        print("Weather Condition:", data["weather"][0]["description"])
    else:
        print("Invalid city name or API error.")

def main():
    print("Weather Forecast Application")
    print("-----------------------------")
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
