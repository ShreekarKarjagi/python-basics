"""
LESSON 5: Functions
===================
A function is a reusable block of code with a name. You give it inputs
(parameters) and it can give back an output (with `return`).

You've already been writing functions in every exercise! This lesson
explains how they work in more detail.

Run this file:  python 05_functions.py
"""
from checker import check, summary

# ---------------------------------------------------------------
# EXAMPLES
# ---------------------------------------------------------------
print("=== Examples ===")


# Define a function with `def`, then call it by name with ()
def say_hello():
    print("Hello!")


say_hello()
say_hello()


# Parameters are the inputs. `return` sends a value back to the caller.
def add(a, b):
    return a + b


result = add(3, 4)
print("3 + 4 =", result)


# print vs return: print SHOWS a value, return GIVES it back to use later.
def prints_double(x):
    print(x * 2)      # shows it, but returns None


def returns_double(x):
    return x * 2      # gives it back


y = returns_double(5) + 1   # 11, we can keep using the value
print("y:", y)


# Default parameter values
def greet(name, greeting="Hi"):
    return f"{greeting}, {name}!"


print(greet("Lee"))                  # Hi, Lee!
print(greet("Lee", "Good morning"))  # Good morning, Lee!
print(greet(greeting="Yo", name="Lee"))  # keyword arguments, any order


# Returning multiple values (as a tuple)
def min_and_max(numbers):
    return min(numbers), max(numbers)


low, high = min_and_max([4, 1, 9])
print("low:", low, "high:", high)


# A docstring describes what a function does
def area_of_rectangle(width, height):
    """Return the area of a rectangle."""
    return width * height


print(area_of_rectangle(3, 5))


# Scope: variables created inside a function only exist inside it
def make_secret():
    secret = 42
    return secret


print(make_secret())
# print(secret)   # <- this would crash: NameError, `secret` only lived inside the function


# Functions can call other functions
def square(x):
    return x * x


def sum_of_squares(a, b):
    return square(a) + square(b)


print(sum_of_squares(3, 4))   # 25


# Recursion: a function that calls itself (an advanced idea, just a taste)
def countdown(n):
    if n == 0:
        return "Go!"
    return str(n) + " " + countdown(n - 1)


print(countdown(3))   # 3 2 1 Go!

# ---------------------------------------------------------------
# EXERCISES
# ---------------------------------------------------------------
# This time YOU write the whole function, including the `def` line.
# Each TODO tells you the name and parameters the checks expect.

# TODO 1: write a function `celsius_to_fahrenheit(c)` that returns c * 9 / 5 + 32


# TODO 2: write a function `average(numbers)` that returns the average of a
# list of numbers. Hint: sum(numbers) / len(numbers)


# TODO 3: write a function `power(base, exponent=2)` that returns base to the
# power of exponent. If exponent isn't given, it should square the base.


# TODO 4: write a function `describe_number(n)` that returns a string like
# "7 is odd" or "4 is even". Reuse what you learned about % and f-strings.


# TODO 5: write a function `largest(numbers)` that returns the largest number
# in a list WITHOUT using the built-in max(). Use a loop.


# ---------------------------------------------------------------
# CHECKS
# ---------------------------------------------------------------
print("\n=== Checks ===")
check("celsius_to_fahrenheit(100)", lambda: celsius_to_fahrenheit(100), 212.0)
check("celsius_to_fahrenheit(0)", lambda: celsius_to_fahrenheit(0), 32.0)
check("average([2, 4, 6])", lambda: average([2, 4, 6]), 4.0)
check("power(3)", lambda: power(3), 9)
check("power(2, 5)", lambda: power(2, 5), 32)
check("describe_number(7)", lambda: describe_number(7), "7 is odd")
check("describe_number(4)", lambda: describe_number(4), "4 is even")
check("largest([3, 9, 2, 7])", lambda: largest([3, 9, 2, 7]), 9)
check("largest([-5, -2, -8])", lambda: largest([-5, -2, -8]), -2)
summary()
