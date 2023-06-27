# %%
"""
Solution 1a
Basic functionality:
This script shall only have one call to the start_washing() function to execute.

start_washing() function shall return an integer containing total energy consumed

Each internal function has following characteristics:
- input of the previous accumulated energy,
- printout how many minutes it takes (e.g. “Heating water -> 20 minutes”)
- output with previous + consumed energy within this step
"""

# Create a dictionary for each function
pump_water = {"duration": 10, "energy_consumption": 5, "energy_consumption_eco": 5}

first_spin = {"duration": 5, "energy_consumption": 15, "energy_consumption_eco": 15}

heat_water = {"duration": 20, "energy_consumption": 1300, "energy_consumption_eco": 900}

rinse = {"duration": 15, "energy_consumption": 80, "energy_consumption_eco": 40}

final_spin = {"duration": 40, "energy_consumption": 500, "energy_consumption_eco": 800}


# Washing machine functionalities
def start_washing():
    # Create a list for energy consumption
    accumulated_energy = []

    # Create a list for spent time
    duration = []

    # Pumping water
    print("Previously consumed energy:", sum(accumulated_energy), "Jules")
    accumulated_energy.append(pump_water["energy_consumption"])
    duration.append(pump_water["duration"])
    print("Pumping water -> 10 minutes")
    print("Consumed energy:", sum(accumulated_energy), "Jules")
    print()

    # First spin
    print("Previously consumed energy:", sum(accumulated_energy), "Jules")
    accumulated_energy.append(first_spin["energy_consumption"])
    duration.append(first_spin["duration"])
    print("Spinning -> 5 minutes")
    print("Consumed energy:", sum(accumulated_energy), "Jules")
    print()

    # Heating water
    print("Previously consumed energy:", sum(accumulated_energy), "Jules")
    accumulated_energy.append(heat_water["energy_consumption"])
    duration.append(heat_water["duration"])
    print("Heating water -> 10 minutes")
    print("Consumed energy:", sum(accumulated_energy), "Jules")
    print()

    # Rinsing
    print("Previously consumed energy:", sum(accumulated_energy), "Jules")
    accumulated_energy.append(rinse["energy_consumption"])
    duration.append(rinse["duration"])
    print("Rinsing -> 15 minutes")
    print("Consumed energy:", sum(accumulated_energy), "Jules")
    print()

    # Final spin
    print("Previously consumed energy:", sum(accumulated_energy), "Jules")
    accumulated_energy.append(final_spin["energy_consumption"])
    duration.append(final_spin["duration"])
    print("Spinning -> 40 minutes")
    print("Consumed energy:", sum(accumulated_energy), "Jules")

    # Return the total energy consumed
    return sum(accumulated_energy)


# Call the function
start_washing()


# %%
"""
Solution 1b
Define each washing step as a tuple with name, duration, 
and energy consumption
"""
washing_steps = [
    ("Pumping water", 10, 5),
    ("First spin", 5, 15),
    ("Heating water", 20, 1300),
    ("Rinsing", 15, 80),
    ("Final spin", 40, 500),
]


# Define a function to execute the washing steps and calculate the total energy consumption
def start_washing():
    accumulated_energy = 0
    duration = 0

    # Iterate through each washing step
    for step in washing_steps:
        name, step_duration, energy_consumption = step
        print("Previously consumed energy:", accumulated_energy, "Jules")
        accumulated_energy += energy_consumption
        duration += step_duration
        print(name, "->", step_duration, "minutes")
        print("Consumed energy:", accumulated_energy, "Jules")
        print()

    # Return the total energy consumed
    return accumulated_energy


# Call the function
start_washing()


# %%
"""
Solution 1c

By defining pump_water as a separate method at the same indentation level as start_washing, it becomes an independent method that can be called separately from the start_washing method. This allows for more flexibility in the usage of the WashingMachine class.
"""


class WashingMachine:
    def __init__(self):
        self.duration = 0
        self.energy_consumption = 0

    def start_washing(self):
        self.pump_water()
        self.first_spin()
        self.heating_water()
        self.rinsing()
        self.final_spin()
        return self.energy_consumption

    # Pumping water
    def pump_water(self):
        print(f"Previously consumed energy: {self.energy_consumption} Jules")
        print("Pumping water -> 10 minutes")
        self.duration += 10
        self.energy_consumption += 5
        print(f"Consumed energy: {self.energy_consumption} Jules")
        print()

    # First spin
    def first_spin(self):
        print(f"Previously consumed energy: {self.energy_consumption} Jules")
        print("Spinning -> 5 minutes")
        self.duration += 5
        self.energy_consumption += 15
        print(f"Consumed energy: {self.energy_consumption} Jules")
        print()

    # Heating water
    def heating_water(self):
        print(f"Previously consumed energy: {self.energy_consumption} Jules")
        print("Heating water -> 10 minutes")
        self.duration += 20
        self.energy_consumption += 1300
        print(f"Consumed energy: {self.energy_consumption} Jules")
        print()

    # Rinsing
    def rinsing(self):
        print(f"Previously consumed energy: {self.energy_consumption} Jules")
        print("Rinsing -> 15 minutes")
        self.duration += 15
        self.energy_consumption += 80
        print(f"Consumed energy: {self.energy_consumption} Jules")
        print()

    # Final spin
    def final_spin(self):
        print(f"Previously consumed energy: {self.energy_consumption} Jules")
        print("Spinning -> 40 minutes")
        self.duration += 40
        self.energy_consumption += 500
        print(f"Consumed energy: {self.energy_consumption} Jules")
        print()


# Test the function
Bosh = WashingMachine()
Bosh.start_washing()


# %%
"""
Solution 2a
Extended functionality: 
start_washing() function

- Ask for input to select eco or normal mode

- Shall return a tuple with an integer containing total energy consumed and the total time used
"""

# Create a dictionary for each function
pump_water = {"duration": 10, "energy_consumption": 5, "energy_consumption_eco": 5}

first_spin = {"duration": 5, "energy_consumption": 15, "energy_consumption_eco": 15}

heat_water = {"duration": 20, "energy_consumption": 1300, "energy_consumption_eco": 900}

rinse = {"duration": 15, "energy_consumption": 80, "energy_consumption_eco": 40}

final_spin = {"duration": 40, "energy_consumption": 500, "energy_consumption_eco": 800}


# Washing machine functionalities
def start_washing():
    # Create a list for energy consumption
    accumulated_energy = []

    # Create a list for spent time
    duration = []

    # Prompt user for washing mode: eco or normal
    washing_mode = input("Choose washing mode: eco or normal").lower().strip()

    if washing_mode == "eco":
        # Pumping water
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        accumulated_energy.append(pump_water["energy_consumption_eco"])
        duration.append(pump_water["duration"])
        print("Pumping water -> 10 minutes")
        print("Consumed energy:", sum(accumulated_energy), "Jules")
        print()
        # First spin
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        accumulated_energy.append(first_spin["energy_consumption_eco"])
        duration.append(first_spin["duration"])
        print("Spinning -> 5 minutes")
        print("Conesumed energy:", sum(accumulated_energy), "Jules")
        print()
        # Heating water
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        accumulated_energy.append(heat_water["energy_consumption_eco"])
        duration.append(heat_water["duration"])
        print("Heating water -> 10 minutes")
        print("Consumed energy:", sum(accumulated_energy), "Jules")
        print()
        # Rinsing
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        accumulated_energy.append(rinse["energy_consumption_eco"])
        duration.append(rinse["duration"])
        print("Rinsing -> 15 minutes")
        print("Consumed energy:", sum(accumulated_energy), "Jules")
        print()
        # Final spin
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        accumulated_energy.append(final_spin["energy_consumption_eco"])
        duration.append(final_spin["duration"])
        print("Spinning -> 40 minutes")
        print("Consumed energy:", sum(accumulated_energy), "Jules")

        # Create a tuple for consumed energy and spend time
        results = (int(sum(accumulated_energy)), int(sum(duration)))
        return results

    elif washing_mode == "normal":
        # Pumping water
        print("Previously accumulated energy:", sum(accumulated_energy), "Jules")
        accumulated_energy.append(pump_water["energy_consumption"])
        duration.append(pump_water["duration"])
        print("Pumping water -> 10 minutes")
        print("Consumed energy:", sum(accumulated_energy), "Jules")
        print()
        # First spin
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        accumulated_energy.append(first_spin["energy_consumption"])
        duration.append(first_spin["duration"])
        print("Spinning -> 5 minutes")
        print("Conesumed energy:", sum(accumulated_energy), "Jules")
        print()
        # Heating water
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        accumulated_energy.append(heat_water["energy_consumption"])
        duration.append(heat_water["duration"])
        print("Heating water -> 10 minutes")
        print("Consumed energy:", sum(accumulated_energy), "Jules")
        print()
        # Rinsing
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        accumulated_energy.append(rinse["energy_consumption"])
        duration.append(rinse["duration"])
        print("Rinsing -> 15 minutes")
        print("Consumed energy:", sum(accumulated_energy), "Jules")
        print()
        # Final spin
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        accumulated_energy.append(final_spin["energy_consumption"])
        duration.append(final_spin["duration"])
        print("Spinning -> 40 minutes")
        print("Consumed energy:", sum(accumulated_energy), "Jules")

        # Create a tuple for consumed energy and spend time
        results = (int(sum(accumulated_energy)), int(sum(duration)))
        return results

    else:
        print("Please enter washing mode: eco or normal")
        start_washing()


# Call the function
start_washing()


# %%
""" 
Solution 2b
Define each washing step as a tuple with name, duration, 
and energy consumption
"""
washing_steps = [
    ("Pumping water", 10, 5),
    ("First spin", 5, 15),
    ("Heating water", 20, 1300),
    ("Rinsing", 15, 80),
    ("Final spin", 40, 500),
]
# Define each washing step (eco) as a tuple with name, duration, and energy consumption
washing_steps_eco = [
    ("Pumping water", 10, 5),
    ("First spin", 5, 15),
    ("Heating water", 20, 900),
    ("Rinsing", 15, 40),
    ("Final spin", 40, 800),
]


# Define a function to execute the washing steps and calculate the total energy consumption
def start_washing():
    accumulated_energy = 0
    duration = 0
    washing_mode = input("Choose washing mode: eco or normal").lower().strip()

    if washing_mode == "eco":
        # Iterate through each washing step
        for step in washing_steps_eco:
            name, step_duration, energy_consumption = step
            print("Previously consumed energy:", accumulated_energy, "Jules")
            accumulated_energy += energy_consumption
            duration += step_duration
            print(name, "->", step_duration, "minutes")
            print("Consumed energy:", accumulated_energy, "Jules")
            print()

        # Return the total energy consumed and time spent
        results = (accumulated_energy, duration)
        return results

    elif washing_mode == "normal":
        # Iterate through each washing step
        for step in washing_steps:
            name, step_duration, energy_consumption = step
            print("Previously consumed energy:", accumulated_energy, "Jules")
            accumulated_energy += energy_consumption
            duration += step_duration
            print(name, "->", step_duration, "minutes")
            print("Consumed energy:", accumulated_energy, "Jules")
            print()

        # Return the total energy consumed and time spent
        results = (accumulated_energy, duration)
        return results

    else:
        print("Please enter washing mode: eco or normal")
        start_washing()


# Call the function
start_washing()


# %%
"""
Solution 2c
"""


class WashingMachine:
    def __init__(self):
        self.duration = 0
        self.energy_consumption = 0

    def start_washing(self):
        self.washing_mode_eco = (
            input("Would you like to use ECO wash? (y/n)").strip().lower()
        )
        self.pump_water()
        self.first_spin()
        self.heating_water()
        self.rinsing()
        self.final_spin()
        return (self.energy_consumption, self.duration)

    # Pumping water
    def pump_water(self):
        print(f"Previously consumed energy: {self.energy_consumption} Jules")
        print("Pumping water -> 10 minutes")
        self.duration += 10
        if self.washing_mode_eco == "y":
            self.energy_consumption += 5
        else:
            self.energy_consumption += 5
        print(f"Consumed energy: {self.energy_consumption} Jules")
        print()

    # First spin
    def first_spin(self):
        print(f"Previously consumed energy: {self.energy_consumption} Jules")
        print("Spinning -> 5 minutes")
        self.duration += 5
        if self.washing_mode_eco == "y":
            self.energy_consumption += 15
        else:
            self.energy_consumption += 15
        print(f"Consumed energy: {self.energy_consumption} Jules")
        print()

    # Heating water
    def heating_water(self):
        print(f"Previously consumed energy: {self.energy_consumption} Jules")
        print("Heating water -> 10 minutes")
        self.duration += 20
        if self.washing_mode_eco == "y":
            self.energy_consumption += 900
        else:
            self.energy_consumption += 1300
        print(f"Consumed energy: {self.energy_consumption} Jules")
        print()

    # Rinsing
    def rinsing(self):
        print(f"Previously consumed energy: {self.energy_consumption} Jules")
        print("Rinsing -> 15 minutes")
        self.duration += 15
        if self.washing_mode_eco == "y":
            self.energy_consumption += 40
        else:
            self.energy_consumption += 80
        print(f"Consumed energy: {self.energy_consumption} Jules")
        print()

    # Final spin
    def final_spin(self):
        print(f"Previously consumed energy: {self.energy_consumption} Jules")
        print("Spinning -> 40 minutes")
        self.duration += 40
        if self.washing_mode_eco == "y":
            self.energy_consumption += 800
        else:
            self.energy_consumption += 500
        print(f"Consumed energy: {self.energy_consumption} Jules")
        print()


# Test the function
Bosh = WashingMachine()
Bosh.start_washing()


# %%
"""
Solution 3a
Each internal function has following characteristics:
- Input of the previous accumulated energy, the so far consumed time, 
and a Boolean to indicate whether is eco mode or not

- Printout how many minutes it takes (e.g. “Heating water -> 20 minutes”)

- Output with previous + consumed energy within this step, 
and the previous + consumed time
"""

# Create a dictionary for each function
pump_water = {"duration": 10, "energy_consumption": 5, "energy_consumption_eco": 5}

first_spin = {"duration": 5, "energy_consumption": 15, "energy_consumption_eco": 15}

heat_water = {"duration": 20, "energy_consumption": 1300, "energy_consumption_eco": 900}

rinse = {"duration": 15, "energy_consumption": 80, "energy_consumption_eco": 40}

final_spin = {"duration": 40, "energy_consumption": 500, "energy_consumption_eco": 800}


# Washing machine functionalities
def start_washing():
    # Create a list for energy consumption
    accumulated_energy = []

    # Create a list for spent time
    duration = []

    # Prompt user for washing mode: eco or normal
    washing_mode = input("Choose washing mode: eco or normal").lower().strip()

    if washing_mode == "eco":
        print("Washing mode: ECO")
        print()

        # Pumping water
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        print("Previously spent time:", sum(duration), "minutes")
        accumulated_energy.append(pump_water["energy_consumption_eco"])
        duration.append(pump_water["duration"])
        print("Pumping water -> 10 minutes")
        print("Consumed energy:", sum(accumulated_energy), "Jules")
        print("Spent time:", sum(duration), "minutes")
        print()

        # First spin
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        print("Previously spent time:", sum(duration), "minutes")
        accumulated_energy.append(first_spin["energy_consumption_eco"])
        duration.append(first_spin["duration"])
        print("Spinning -> 5 minutes")
        print("Conesumed energy:", sum(accumulated_energy), "Jules")
        print("Spent time:", sum(duration), "minutes")
        print()

        # Heating water
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        print("Previously spent time:", sum(duration), "minutes")
        accumulated_energy.append(heat_water["energy_consumption_eco"])
        duration.append(heat_water["duration"])
        print("Heating water -> 10 minutes")
        print("Consumed energy:", sum(accumulated_energy), "Jules")
        print("Spent time:", sum(duration), "minutes")
        print()

        # Rinsing
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        print("Previously spent time:", sum(duration), "minutes")
        accumulated_energy.append(rinse["energy_consumption_eco"])
        duration.append(rinse["duration"])
        print("Rinsing -> 15 minutes")
        print("Consumed energy:", sum(accumulated_energy), "Jules")
        print("Spent time:", sum(duration), "minutes")
        print()

        # Final spin
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        print("Previously spent time:", sum(duration), "minutes")
        accumulated_energy.append(final_spin["energy_consumption_eco"])
        duration.append(final_spin["duration"])
        print("Spinning -> 40 minutes")
        print("Consumed energy:", sum(accumulated_energy), "Jules")
        print("Spent time:", sum(duration), "minutes")

        # Create a tuple for consumed energy and spend time
        results = (int(sum(accumulated_energy)), int(sum(duration)))
        return results

    elif washing_mode == "normal":
        print("Washing mode: NORMAL")
        print()

        # Pumping water
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        print("Previously spent time:", sum(duration), "minutes")
        accumulated_energy.append(pump_water["energy_consumption"])
        duration.append(pump_water["duration"])
        print("Pumping water -> 10 minutes")
        print("Consumed energy:", sum(accumulated_energy), "Jules")
        print("Spent time:", sum(duration), "minutes")
        print()

        # First spin
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        print("Previously spent time:", sum(duration), "minutes")
        accumulated_energy.append(first_spin["energy_consumption"])
        duration.append(first_spin["duration"])
        print("Spinning -> 5 minutes")
        print("Conesumed energy:", sum(accumulated_energy), "Jules")
        print("Spent time:", sum(duration), "minutes")
        print()

        # Heating water
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        print("Previously spent time:", sum(duration), "minutes")
        accumulated_energy.append(heat_water["energy_consumption"])
        duration.append(heat_water["duration"])
        print("Heating water -> 10 minutes")
        print("Consumed energy:", sum(accumulated_energy), "Jules")
        print("Spent time:", sum(duration), "minutes")
        print()

        # Rinsing
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        print("Previously spent time:", sum(duration), "minutes")
        accumulated_energy.append(rinse["energy_consumption"])
        duration.append(rinse["duration"])
        print("Rinsing -> 15 minutes")
        print("Consumed energy:", sum(accumulated_energy), "Jules")
        print("Spent time:", sum(duration), "minutes")
        print()

        # Final spin
        print("Previously consumed energy:", sum(accumulated_energy), "Jules")
        print("Previously spent time:", sum(duration), "minutes")
        accumulated_energy.append(final_spin["energy_consumption"])
        duration.append(final_spin["duration"])
        print("Spinning -> 40 minutes")
        print("Consumed energy:", sum(accumulated_energy), "Jules")
        print("Spent time:", sum(duration), "minutes")

        # Create a tuple for consumed energy and spend time
        results = (int(sum(accumulated_energy)), int(sum(duration)))
        return results

    else:
        print("Please enter washing mode: eco or normal")
        start_washing()


# Call the function
start_washing()

# %%
"""
Solution 3b
Define each washing step as a tuple with name, duration, 
and energy consumption
"""
washing_steps = [
    ("Pumping water", 10, 5),
    ("First spin", 5, 15),
    ("Heating water", 20, 1300),
    ("Rinsing", 15, 80),
    ("Final spin", 40, 500),
]
# Define each washing step (eco) as a tuple with name, duration, and energy consumption
washing_steps_eco = [
    ("Pumping water", 10, 5),
    ("First spin", 5, 15),
    ("Heating water", 20, 900),
    ("Rinsing", 15, 40),
    ("Final spin", 40, 800),
]


# Define a function to execute the washing steps and calculate the total energy consumption
def start_washing():
    accumulated_energy = 0
    duration = 0
    washing_mode_eco = input("Would you like to use ECO wash? (y/n)").lower().strip()

    if washing_mode_eco == "y":
        print("Washing mode: ECO")
        print()
        # Iterate through each washing step
        for step in washing_steps_eco:
            name, step_duration, energy_consumption = step
            print("Previously consumed energy:", accumulated_energy, "Jules")
            print("Previously spent time:", duration, "minutes")
            accumulated_energy += energy_consumption
            duration += step_duration
            print(name, "->", step_duration, "minutes")
            print("Consumed energy:", accumulated_energy, "Jules")
            print("Spent time:", duration, "minutes")
            print()

        # Return the total energy consumed and time spent
        results = (int(accumulated_energy), int(duration))
        return results

    elif washing_mode_eco == "n":
        print("Washing mode: NORMAL")
        print()
        # Iterate through each washing step
        for step in washing_steps:
            name, step_duration, energy_consumption = step
            print("Previously consumed energy:", accumulated_energy, "Jules")
            print("Previously spent time:", duration, "minutes")
            accumulated_energy += energy_consumption
            duration += step_duration
            print(name, "->", step_duration, "minutes")
            print("Consumed energy:", accumulated_energy, "Jules")
            print("Spent time:", duration, "minutes")
            print()

        # Return the total energy consumed and time spent
        results = (int(accumulated_energy), int(duration))
        return results

    else:
        print("Would you like to use ECO wash? (y/n)")
        start_washing()


# Call the function
start_washing()


# %%
"""
Solution 3c
"""


class WashingMachine:
    def __init__(self):
        self.duration = 0
        self.energy_consumption = 0

    def start_washing(self):
        self.washing_mode_eco = (
            input("Would you like to use ECO wash? (y/n)").strip().lower()
        )
        if self.washing_mode_eco == "y":
            print(f"Washing mode: ECO")

        else:
            print(f"Washing mode: NORMAL")

        print()
        self.pump_water()
        self.first_spin()
        self.heating_water()
        self.rinsing()
        self.final_spin()
        return (self.energy_consumption, self.duration)

    # Pumping water
    def pump_water(self):
        print(f"Previously consumed energy: {self.energy_consumption} Jules")
        print(f"Previously spent time: {self.duration} minutes")
        print("Pumping water -> 10 minutes")
        self.duration += 10
        if self.washing_mode_eco == "y":
            self.energy_consumption += 5
        else:
            self.energy_consumption += 5
        print(f"Consumed energy: {self.energy_consumption} Jules")
        print(f"Spent time: {self.duration} minutes")
        print()

    # First spin
    def first_spin(self):
        print(f"Previously consumed energy: {self.energy_consumption} Jules")
        print(f"Previously spent time: {self.duration} minutes")
        print("Spinning -> 5 minutes")
        self.duration += 5
        if self.washing_mode_eco == "y":
            self.energy_consumption += 15
        else:
            self.energy_consumption += 15
        print(f"Consumed energy: {self.energy_consumption} Jules")
        print(f"Spent time: {self.duration} minutes")
        print()

    # Heating water
    def heating_water(self):
        print(f"Previously consumed energy: {self.energy_consumption} Jules")
        print(f"Previously spent time: {self.duration} minutes")
        print("Heating water -> 10 minutes")
        self.duration += 20
        if self.washing_mode_eco == "y":
            self.energy_consumption += 900
        else:
            self.energy_consumption += 1300
        print(f"Consumed energy: {self.energy_consumption} Jules")
        print(f"Spent time: {self.duration} minutes")
        print()

    # Rinsing
    def rinsing(self):
        print(f"Previously consumed energy: {self.energy_consumption} Jules")
        print(f"Previously spent time: {self.duration} minutes")
        print("Rinsing -> 15 minutes")
        self.duration += 15
        if self.washing_mode_eco == "y":
            self.energy_consumption += 40
        else:
            self.energy_consumption += 80
        print(f"Consumed energy: {self.energy_consumption} Jules")
        print(f"Spent time: {self.duration} minutes")
        print()

    # Final spin
    def final_spin(self):
        print(f"Previously consumed energy: {self.energy_consumption} Jules")
        print(f"Previously spent time: {self.duration} minutes")
        print("Spinning -> 40 minutes")
        self.duration += 40
        if self.washing_mode_eco == "y":
            self.energy_consumption += 800
        else:
            self.energy_consumption += 500
        print(f"Consumed energy: {self.energy_consumption} Jules")
        print(f"Spent time: {self.duration} minutes")
        print()


# Test the function
Bosh = WashingMachine()
Bosh.start_washing()

# %%
"""
Solution 3d
"""


class WashingMachine:
    def __init__(self):
        self.duration = 0
        self.energy_consumption = 0

    def start_washing(self):
        self.washing_mode_eco = (
            input("Would you like to use ECO wash? (y/n)").strip().lower()
        )
        if self.washing_mode_eco == "y":
            print(f"Washing mode: ECO")
        else:
            print(f"Washing mode: NORMAL")
        print()
        print(f"Previously consumed energy: {self.energy_consumption} Jules")
        print(f"Previously spent time: {self.duration} minutes")
        print()
        self.pump_water()
        self.first_spin()
        self.heating_water()
        self.rinsing()
        self.final_spin()
        print(f"Consumed energy: {self.energy_consumption} Jules")
        print(f"Spent time: {self.duration} minutes")
        return (self.energy_consumption, self.duration)

    # Pumping water
    def pump_water(self):
        self.duration += 10
        if self.washing_mode_eco == "y":
            self.energy_consumption += 5
        else:
            self.energy_consumption += 5

    # First spin
    def first_spin(self):
        self.duration += 5
        if self.washing_mode_eco == "y":
            self.energy_consumption += 15
        else:
            self.energy_consumption += 15

    # Heating water
    def heating_water(self):
        self.duration += 20
        if self.washing_mode_eco == "y":
            self.energy_consumption += 900
        else:
            self.energy_consumption += 1300

    # Rinsing
    def rinsing(self):
        self.duration += 15
        if self.washing_mode_eco == "y":
            self.energy_consumption += 40
        else:
            self.energy_consumption += 80

    # Final spin
    def final_spin(self):
        self.duration += 40
        if self.washing_mode_eco == "y":
            self.energy_consumption += 800
        else:
            self.energy_consumption += 500


# Test the function
Bosh = WashingMachine()
Bosh.start_washing()


# %%
"""
Solution 3e
"""


class WashingMachine:
    def __init__(self):
        self.duration = 0
        self.energy_consumption = 0

    def start_washing(self):
        self.washing_mode_eco = (
            input("Would you like to use ECO wash? (y/n)").strip().lower()
        )
        print(f"Washing mode: {'ECO' if self.washing_mode_eco == 'y' else 'NORMAL'}")
        print()
        print(f"Previously consumed energy: {self.energy_consumption} Jules")
        print(f"Previously spent time: {self.duration} minutes")
        print()
        self.pump_water(5)
        self.first_spin(15)
        self.heating_water(900, 1300)
        self.rinsing(40, 80)
        self.final_spin(800, 500)
        print(f"Consumed energy: {self.energy_consumption} Jules")
        print(f"Spent time: {self.duration} minutes")
        return (self.energy_consumption, self.duration)

    def pump_water(self, energy):
        self.duration += 10
        self.energy_consumption += energy

    def first_spin(self, energy):
        self.duration += 5
        self.energy_consumption += energy

    def heating_water(self, energy_eco, energy_normal):
        self.duration += 20
        self.energy_consumption += (
            energy_eco if self.washing_mode_eco == "y" else energy_normal
        )

    def rinsing(self, energy_eco, energy_normal):
        self.duration += 15
        self.energy_consumption += (
            energy_eco if self.washing_mode_eco == "y" else energy_normal
        )

    def final_spin(self, energy_eco, energy_normal):
        self.duration += 40
        self.energy_consumption += (
            energy_eco if self.washing_mode_eco == "y" else energy_normal
        )


# Test the function
Bosh = WashingMachine()
Bosh.start_washing()


# %%
"""
Solution 3f
"""


class WashingMachine:
    def __init__(self):
        self.duration = 0
        self.energy_consumption = 0
        self.energy_mapping = {
            "pump_water": 5,
            "first_spin": 15,
            "heating_water": {"y": 900, "n": 1300},
            "rinsing": {"y": 40, "n": 80},
            "final_spin": {"y": 800, "n": 500},
        }

    def start_washing(self):
        self.washing_mode_eco = (
            input("Would you like to use ECO wash? (y/n)").strip().lower()
        )
        print(f"Washing mode: {'ECO' if self.washing_mode_eco == 'y' else 'NORMAL'}")
        print()
        print(f"Previously consumed energy: {self.energy_consumption} Jules")
        print(f"Previously spent time: {self.duration} minutes")
        print()

        self.run_step("pump_water", 10)
        self.run_step("first_spin", 5)
        self.run_step("heating_water", 20)
        self.run_step("rinsing", 15)
        self.run_step("final_spin", 40)

        print(f"Consumed energy: {self.energy_consumption} Jules")
        print(f"Spent time: {self.duration} minutes")
        return (self.energy_consumption, self.duration)

    def run_step(self, step, duration):
        self.duration += duration
        energy_consumption = self.energy_mapping[step]

        if isinstance(energy_consumption, dict):
            energy_consumption = energy_consumption[self.washing_mode_eco]

        self.energy_consumption += energy_consumption


# Test the function
Bosh = WashingMachine()
Bosh.start_washing()


# %%

