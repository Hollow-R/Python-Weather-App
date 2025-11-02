import requests

API_KEY = "..."     #Your API key goes here
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",
        "lang": "eng"
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        city = data["name"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]

        print(f"\nWeather for {city} :")
        print(f"Temperature: {temp}°C")
        print(f"Felt Temperature: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Status: {desc.capitalize()}\n")
    else:
        print("Error\n")

def main():
    print("=== Weather Application ===")
    while True:
        city = input("City name (press q to exit): ")
        if city.lower() == "q":
            print("bye")
            break
        get_weather(city)

if __name__ == "__main__":
    main()

        
