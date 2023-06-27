# %%
# Print country data
def print_country_data(country_data):
    print(f"Holidays:")
    print(f"{country_data}")
    print(f"Number of Holidays:")
    print(f"{len(country_data)}")
    # print(f"Type:")
    # print(f"{type(country_data)}")
    print("----------------------------------------")


# Print main country information
def print_country_object(country_object):
    print("Country Object Info:")
    print(country_object.__str__())
    # print(f"Type:")
    # print(f"{type(country_object)}")
    print("----------------------------------------")


"""
Define a function that uses a list of Holiday objects within a year and return the month with most holidays
"""


# Get the holidays date list from country data
# date_list = [d['date'] for d in country_data]
def get_month_with_most_holidays(country_data):
    from datetime import datetime
    from collections import Counter

    date_list = []
    for d in country_data:
        date_list.append(d["date"])

    print(f"Holiday Dates:")
    print(f"{date_list}")
    print("----------------------------------------")

    month_list = []
    for date in date_list:
        month = datetime.strptime(date, "%Y-%m-%d").strftime("%B")
        month_list.append(month)

    print(f"Holiday Months:")
    print(f"{month_list}")

    # Count the months using Counter
    month_counts = Counter(month_list)
    print(f"Number of Holidays in Each Month:")
    print(f"{month_counts}")

    # Find the month(s) with most holidays
    highest_count = month_counts.most_common(1)[0][1]

    most_common_months = []
    for month, count in month_counts.most_common():
        if count == highest_count:
            most_common_months.append(month)

    print(f"Month(s) with Most Holidays:")
    print(f"{most_common_months}")
    print("----------------------------------------")
    # return f"Month(s) with Most Holidays: {most_common_months}"


"""
Define a function to call LongWeekend endpoint and calculate which country (within a list of given countries) has more long weekend at some year.

E.g. getBestCountryForHolidays(year: int, ["FI", "FR", "GB", "IT"] )
"""


def get_countries_data(country_codes, holiday_year):
    from library import apifunctions

    countries_data = []
    for country_code in country_codes:
        countries_data.append(
            apifunctions.get_long_weekends(holiday_year, country_code)
        )

    return countries_data


def print_long_weekends_for_countries(holiday_year, country_codes, countries_data):
    # most_long_weekend = 0
    # most_long_weekend_list = []

    print()
    print(f"Long Weekends for {country_codes} in {holiday_year}:")
    for country_code in range(0, len(country_codes)):
        print(f"{country_codes[country_code]}: {len(countries_data[country_code])}")
        print(f"{countries_data[country_code]}")
        print()


def get_best_country_for_holidays(countries_data, country_codes):
    long_weekends_dict = {}
    for country_code in range(len(country_codes)):
        number_of_long_weekends = len(countries_data[country_code])
        long_weekends_dict.update({country_code: number_of_long_weekends})

    print(f"Long Weekends:")
    print(f"{country_codes}")
    print(long_weekends_dict)
    print("----------------------------------------")

    most_long_weekends_countries = []
    number_of_long_weekends = 0
    for key, value in long_weekends_dict.items():
        if value > number_of_long_weekends:
            number_of_long_weekends = value
            most_long_weekends_countries = [key]
        elif value == number_of_long_weekends:
            most_long_weekends_countries.append(key)

    most_long_weekends_country_names = [
        country_codes[country] for country in most_long_weekends_countries
    ]
    print(f"Countries with the Most Long Weekends:")
    return f"{', '.join(most_long_weekends_country_names)} - {number_of_long_weekends}"


# %%