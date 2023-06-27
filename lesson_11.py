# %%
"""
Homework S23, Closures, Decorators and Special Methods ReDI School 
"""
"""
Exercise 1:
Closure - Calculator Create a closure function called calculator that performs basic arithmetic operations. The closure should return a function that takes two numbers and performs a specified operation on them. 

Subtasks: 
	1. Implement the calculator closure function.
	2. Inside the closure, define the nested function operate() that takes two numbers and an operation as arguments. 
	3. In the operate() function, perform the specified operation on the given numbers. 
	4. Return the result of the operation. 
	5. Create a calculator instance by calling the calculator() function. 
	6. Call the returned function from the calculator instance, providing different numbers and operations, and print the results. 
"""


def calculator():
    def operate(a, b, operator):
        if operator == "+":
            return round(a + b, 2)

        elif operator == "-":
            return round(a - b, 2)

        elif operator == "*":
            return round(a * b, 2)

        elif operator == "/":
            return round(a / b, 2)

        else:
            return f"Please select one of the operators '+', '-', '*', '/'"

    return operate


# Test the function
operation_1 = calculator()
print(operation_1(2, 3, "+"))

operation_2 = calculator()
print(operation_2(2, 3, "-"))

operation_3 = calculator()
print(operation_3(2, 3, "*"))

operation_4 = calculator()
print(operation_4(2, 3, "/"))

operation_5 = calculator()
print(operation_4(2, 3, "f"))

# %%
"""
Exercise 2: 
Decorators - Timer Write a decorator function called timer that measures the execution time of a function and prints the elapsed time. Apply the timer decorator to a function of your choice and test its functionality.
 
Subtasks: 
	- Implement the timer decorator function. 
	- Apply the timer decorator to a function. 
	- Test the decorated function to ensure it prints the elapsed time. 
"""
import time


def timer(func):
    start_time = time.time()
    func
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"The execution time: {elapsed_time}")


@timer
def operate(a, b, operator):
    if operator == "+":
        return round(a + b, 2)

    elif operator == "-":
        return round(a - b, 2)

    elif operator == "*":
        return round(a * b, 2)

    elif operator == "/":
        return round(a / b, 2)

    else:
        return f"Please select one of the operators '+', '-', '*', '/'"

    operate(2, 3, "+")


# %%
"""
Exercise 3: 
Special Methods - Rectangle 
1. Create a class called Rectangle with attributes width and height. Implement the __str__() and __eq__() special methods for the Rectangle class. Test the string representation and equality comparison of Rectangle objects. 

Subtasks: 
- Define the Rectangle class with width and height attributes. 
- Implement the __str__() special method to return a string representation of the rectangle. 
- Implement the __eq__() special method to compare two rectangles for equality. 
- Create multiple Rectangle objects and test the string representation and equality comparison.
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"The width of the rectangle is {self.width} and the height is {self.height}."

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height

        return False


# Test the class
shape_1 = Rectangle(3, 5)
shape_2 = Rectangle(3, 5)
shape_3 = Rectangle(3, 6)
print(shape_1 == shape_2)
print(shape_1 == shape_3)

str(shape_1)


# %%
