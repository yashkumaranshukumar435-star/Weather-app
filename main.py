import argparse
import requests

def get_current_weather(city):
    api_key = 'YOUR_API_KEY'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={{city}}&appid={{api_key}}'
    response = requests.get(url)
    return response.json()


def get_forecast(city):
    api_key = 'YOUR_API_KEY'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={{city}}&appid={{api_key}}'
    response = requests.get(url)
    return response.json()


def main():
    parser = argparse.ArgumentParser(description='Weather App')
    parser.add_argument('city', type=str, help='City to get the weather for')
    parser.add_argument('--forecast', action='store_true', help='Get weather forecast')
    args = parser.parse_args()

    if args.forecast:
        forecast = get_forecast(args.city)
        print(f'Forecast for {{args.city}}: {{forecast}}')
    else:
        current_weather = get_current_weather(args.city)
        print(f'Current weather for {{args.city}}: {{current_weather}}')


if __name__ == '__main__':
    main()