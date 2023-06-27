# %%
import requests


# Get holidays of of a given country and year from api
def get_holidays(year, countryCode):
    url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{countryCode}"
    response = requests.request("GET", url)
    data = response.json()
    return data


def get_long_weekends(year, countryCode):
    # Get long weekends of given countries and a year from api
    url = f"https://date.nager.at/api/v3/LongWeekend/{year}/{countryCode}"
    response = requests.request("GET", url)
    data = response.json()
    return data


# %%