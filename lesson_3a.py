# %%
"""
Write a personal weather assistant. This software would take as an input the forecasted temperature from a sensor and would recommend the corresponding clothes to wear.

Consider the following requirements
- Use the function input() to ask what will be the temperature today and store into a variable
- If the temperature is bellow 12°C you should recommend (using print()) to wear a jacket
- If the temperature is bellow 6°C you should recommend (using print()) to wear a pair of gloves
- If the temperature is bellow 10°C you should recommend (using print()) to wear a scarf
- If the temperature is bellow 8°C you should recommend (using print()) to wear a hat
- If the temperature is over 25°C you should recommend (using print()) to wear a sunglasses
"""
# Prompt the user for the weather temperature
temp = int(input("What's the temperature in Celsius today?"))

# Check the temperature and make clothing recommendations
if temp < 12:
    print("Wear a jacket")

    if temp < 10:
        print("Wear a scarf")

    if temp < 8:
        print("Wear a hat")

    if temp < 6:
        print("Wear a pair of gloves")

elif temp > 25:
    print("Wear a sunglasses")

# Prompt the user for the probability of rain
probability_of_rain = int(input("What's the probability of rain (in %)? "))

# Check the probability of rain and make recommendations
if probability_of_rain >= 50:
    print("Carry an umbrella.")


# %%
"""
A personal weather assistant prompts the user for the temperature and provides recommendations on the type of clothing to wear. It also includes evaluation of the probability of rain and provides an additional recommendation to take an umbrella.
"""


def weather_assistant():
    # Prompt the user for the weather temperature
    temp = int(input("What's the temperature in Celsius today?"))

    # Check the temperature and make clothing recommendations
    if temp < 6:
        print(
            "It's very cold. Wear a warm jacket, a scarf, a hat and a pair of gloves."
        )

    elif temp < 8:
        print("It's cold. Wear a warm jacket, a scarf and a hat.")

    elif temp < 10:
        print("It's chilly. Wear a warm jacket and a scarf.")

    elif temp < 12:
        print("It's cool. Wear a light jacket.")

    elif temp > 25:
        print("It's hot. Wear sunglasses and light clothing.")

    else:
        print("The temperature is moderate. Dress comfortably.")

    # Prompt the user for the probability of rain
    probability_of_rain = int(input("What's the probability of rain (in %)? "))

    # Check the probability of rain and make recommendations
    if probability_of_rain >= 50:
        print("It's likely to rain. Consider carrying an umbrella.")


# Run the function
weather_assistant()

# %%
