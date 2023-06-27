# %%
"""
Task1:
Create a class named Car and let class have brand, model name, construction year as attributes
"""


class Car:
    brand = ""
    model = ""
    year = 0


# %%
"""
Task 2:
Create an Object of the car class and name it car1 with the brand porsche, the model cayenne and a construction year of 2019
"""


class Car:
    brand = ""
    model = ""
    year = 0


# Ferrari 488 GTB (2019)
car1 = Car()
car1.brand = "Ferrari"
car1.model = "488 GTB"
car1.year = 2019

# Porsche 911 Carrera (2022)
car2 = Car()
car2.brand = "Porsche"
car2.model = "911 Carrera"
car2.year = 2022

# Chevrolet Corvette Stingray (2021)
car3 = Car()
car3.brand = "Chevrolet"
car3.model = "Corvette Stingray"
car3.year = 2021

# Ford Mustang Shelby GT500 (2020)
car4 = Car()
car4.brand = "Ford"
car4.model = "Mustang Shelby GT500"
car4.year = 2020

print(car1.brand, car1.model, car1.year)
print(car2.brand, car2.model, car2.year)
print(car3.brand, car3.model, car3.year)
print(car4.brand, car4.model, car4.year)


# %%
"""
Task 3:
Give the class a constructor and repr function and use the repr function to print out the attributes
"""


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __repr__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"


# Test the function
car1 = Car("Ferrari", "488 GTB", 2019)
print(car1.brand, car1.model, car1.year)
print()

car2 = Car("Porsche", "911 Carrera", 2022)
car3 = Car("Chevrolet", "Corvette Stingray", 2021)
car4 = Car("Ford", "Mustang Shelby GT500", 2020)

print(repr(car1))
print(repr(car2))
print(repr(car3))
print(repr(car4))


# %%
