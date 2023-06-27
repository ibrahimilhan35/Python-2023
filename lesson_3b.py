# %%
"""
This code generates a list of leap years from 1980 to 2020

A leap year is a year with an extra day, added to keep the calendar year synchronized with the astronomical year. It occurs every 4 years, except for years divisible by 100 but not by 400.
"""
# Generate a list of years from 1980 to 2020 (inclusive)

years_list = list(range(1980, 2021))
# print(years_list)

# Create an empty list to store leap years
leap_years = []

# Loop through each year in the years_list and check if it's a leap year; if so, add it into the leap_years
for year in years_list:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap_years.append(year)

print(len(leap_years))
print(leap_years)


# %%
"""
Optional:
This code generates a list of leap years from 1980 to 2020 using the list comprehension
"""

leap_years = [
    year
    for year in range(1980, 2021)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
]

print(len(leap_years))
print(leap_years)


# %%
"""
Optional:
This code generates a list of leap years from 1980 to 2020 using the range (0, len()) function in the loop
"""

# Generate a list of years from 1980 to 2020 (inclusive)
years_list = list(range(1980, 2021))
# print(years_list)

# Create an empty list to store leap years
leap_years = []

# Loop through each year in the years_list and check if it's a leap year; if so, add it into the leap_years
for year in range(len(years_list)):
    if years_list[year] % 4 == 0 and (
        years_list[year] % 100 != 0 or years_list[year] % 400 == 0
    ):
        leap_years.append(years_list[year])

print(len(leap_years))
print(leap_years)


# %%
