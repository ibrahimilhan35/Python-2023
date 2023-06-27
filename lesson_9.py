# %%
"""
1. Write a Python program to create a Vehicle class with max_speed and mileage instance attributes. (__init__)

2. Give the Vehicle class a method seating_capacity() that will take capacity as an argument and return the string "The seating capacity of (name of the vehicle) is (capacity)."
"""


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        self.capacity = capacity
        return f"The seating capacity of {self.name} is {str(self.capacity)}."


# Creating an instance of Vehicle
vehicle1 = Vehicle("Trailhawk4X4", "130 mi/hr", "18 mi/gal")
vehicle1.seating_capacity(7)

# %%
"""
3. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

4. Write the method seating_capacity() again with capacity as its argument in the Bus class, and using the keyword super() and the inherited method, return the same string, but set the default capacity to 50. Hint: The mystery_function below has a default value of x set to 5.

def mystery_function(x = 5):
    return x

mystery_function() -> Output: 5
mystery_function(10) -> Output: 10
"""


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        self.capacity = capacity
        return f"The seating capacity of {self.name} is {str(self.capacity)}."


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


# Creating an instance of Bus
vehicle2 = Bus("ExpressCruiser", "65 mi/hr", "12 mi/gal")
vehicle2.seating_capacity()  # Using default capacity of 50
vehicle2.seating_capacity(45)  # Passing a custom capacity of 45


# %%
"""
5. Create a class variable (same as a class attribute) color that will be set to white for every instance of the class Bus.

6. Make sure that all the parts of the solution work with your own print statements and debug if needed. Don't be afraid to look for help on the internet, but try your best to understand the solutions instead of simply copying them.
"""


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        self.capacity = capacity
        return f"The seating capacity of {self.name} is {str(self.capacity)}."


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, color="white"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

        print(f"The color of {self.name} is {self.color}.")

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


vehicle2 = Bus("ExpressCruiser", "65 mi/hr", "12 mi/gal")
vehicle2.seating_capacity()  # Using default capacity of 50
vehicle2.seating_capacity(45)  # Passing a custom capacity of 45


# %%
"""
Bonus: Using another class variable to count the number of buses and an "if" condition, set the color of all Buses to red when at least 5 of them are created.
"""


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        self.capacity = capacity
        return f"The seating capacity of {self.name} is {str(self.capacity)}."


class Bus(Vehicle):
    number_of_buses = 0

    def __init__(self, name, max_speed, mileage, color="white"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

        Bus.number_of_buses += 1
        if Bus.number_of_buses > 5:
            self.color = "red"
            print(f"The color of {self.name} is {self.color}.")


# Creating instances of Bus with different names and attributes
vehicle2 = Bus("ExpressCruiser", "65 mi/hr", "12 mi/gal")
vehicle3 = Bus("CityTransit", "55 mi/hr", "10 mi/gal")
vehicle4 = Bus("RapidMover", "70 mi/hr", "14 mi/gal")
vehicle5 = Bus("MetroRunner", "60 mi/hr", "11 mi/gal")
vehicle6 = Bus("ShuttleStar", "50 mi/hr", "9 mi/gal")
# These should be printed as red
vehicle7 = Bus("TravelLiner", "75 mi/hr", "15 mi/gal")
vehicle8 = Bus("MegaHauler", "45 mi/hr", "8 mi/gal")
vehicle9 = Bus("Transcontinental", "80 mi/hr", "16 mi/gal")
vehicle10 = Bus("UrbanExplorer", "40 mi/hr", "7 mi/gal")
vehicle11 = Bus("CommuterMaster", "85 mi/hr", "17 mi/gal")


# %%
class Vehicle:
    # part 1
    def __init__(self, max_speed, mileage, name):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name

    # part 2
    def seating_capacity(self, capacity):
        return f"The seating capacity of {self.name} is {capacity}."
    
# part 3
class Bus(Vehicle):
    # part 4
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

    # part 5
    color = "white"

    # bonus
    numberOfBuses = 0
    def __init__(self, max_speed, mileage, name):
        super().__init__(max_speed, mileage, name)
        Bus.numberOfBuses += 1
        if Bus.numberOfBuses >= 5:
            Bus.color = "red"


#%%
