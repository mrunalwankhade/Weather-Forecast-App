import requests

API_KEY = "f19c412b0ca5444367b0bc360ececf8a"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filter_data = data["list"]
    nr_values = 8 * forecast_days
    filter_data =  filter_data[:nr_values]
    return filter_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))
