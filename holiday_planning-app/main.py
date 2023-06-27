# %%
from library import user_interactions
from library import apifunctions
from library import holiday
from library import helpers

print("Welcome to Holiday App!")
print()

# Get year and country code from the user
country_code = user_interactions.ask_user_for_country_code()
holiday_year = user_interactions.ask_user_for_year()

# Get holidays data from api
country_data = apifunctions.get_holidays(holiday_year, country_code)

# Print country data
helpers.print_country_data(country_data)

# Create country object
country_object = holiday.Holiday(
    country_data[0],
    country_data[1],
    country_data[2],
    country_data[3],
    country_data[4],
    country_data[5],
    country_data[6],
    country_data[7],
    country_data[8],
)

# Print country object
helpers.print_country_object(country_object)

# Get most holidays month in a given year
helpers.get_month_with_most_holidays(country_data)

# Country codes for api data
country_codes = ["TR", "ES", "IT", "US", "BR", "FR", "DE"]

# Get long weekends data for the countries from api 
countries_data = helpers.get_countries_data(country_codes, holiday_year)

# Print long weekends data for the countries
helpers.print_long_weekends_for_countries(holiday_year, country_codes, countries_data)

# Get the best countries for long weekends within a year
helpers.get_best_country_for_holidays(countries_data, country_codes)


# %%