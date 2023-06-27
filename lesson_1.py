"""
Create a list of dictionaries
list length >= 3
Each dictionary shall contain at least two key-value pairs
Print the output of the dictionaries
"""
# %%
list_of_dictionaries = [
    {"brand": "Ford", "name": "Mustang", "year": "1971", "color": "blue"},
    {
        "event": "FIFA World Cup",
        "year": "2026",
        "stadium": "NRG Stadium",
        "game": "Turkiye vs Brasil",
    },
    {
        "player_name": "Neymar da Silva Santos Júnior",
        "country": "Brasil",
        "position": "forward",
        "games": "708",
        "goals": "437",
    },
]
print(list_of_dictionaries)

# %%
# Optional -> create the same using dict() constructor
list_of_dictionaries = [
    dict(brand="Ford", name="Mustang", year=1971, color="blue"),
    dict(
        event="FIFA World Cup",
        year=2026,
        stadium="NRG Stadium",
        game="Turkiye vs Brasil",
    ),
    dict(
        player_name="Neymar da Silva Santos Júnior",
        country="Brasil",
        position="forward",
        games=708,
        goals=437,
    ),
]

print(list_of_dictionaries)

# %%
# Optional
my_favorite_car = {"brand": "Ford", "name": "Mustang", "year": "1971", "color": "blue"}
my_favorite_event = {
    "event": "FIFA World Cup",
    "year": "2026",
    "stadium": "NRG Stadium",
    "game": "Turkiye vs Brasil",
}
my_favorite_player = {
    "player_name": "Neymar da Silva Santos Júnior",
    "country": "Brasil",
    "position": "forward",
    "games": "708",
    "goals": "437",
}

list_of_dictionaries = [my_favorite_car, my_favorite_event, my_favorite_player]

print(list_of_dictionaries)

# %%
# Using append method
my_favorite_car = {"brand": "Ford", "name": "Mustang", "year": "1971", "color": "blue"}
my_favorite_event = {
    "event": "FIFA World Cup",
    "year": "2026",
    "stadium": "NRG Stadium",
    "game": "Turkiye vs Brasil",
}
my_favorite_player = {
    "player_name": "Neymar da Silva Santos Júnior",
    "country": "Brasil",
    "position": "forward",
    "games": "708",
    "goals": "437",
}

list_of_dictionaries = [my_favorite_car, my_favorite_event]

list_of_dictionaries.append(my_favorite_player)

print(list_of_dictionaries)

# %%
