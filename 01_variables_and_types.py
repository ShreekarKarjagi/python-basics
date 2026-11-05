"""
LESSON 1: Variables and Types
=============================
A variable is a name that holds a value. You create one with `=`.
Python figures out the type for you.

Run this file:  python 01_variables_and_types.py
"""
from checker import check, summary

# ---------------------------------------------------------------
# EXAMPLES: read these, run the file, and change them to experiment
# ---------------------------------------------------------------

# Lines starting with # are comments. Python ignores them.

name = "Ada"          # str   (string = text, in quotes)
age = 20              # int   (whole number)
height = 1.68         # float (decimal number)
is_student = True     # bool  (True or False)
nothing = None        # None  (means "no value")

print("=== Examples ===")
print(name, age, height, is_student, nothing)
print(type(name), type(age), type(height), type(is_student))

# Math operators
print(7 + 2)    # 9    addition
print(7 - 2)    # 5    subtraction
print(7 * 2)    # 14   multiplication
print(7 / 2)    # 3.5  division (always gives a float)
print(7 // 2)   # 3    floor division (drops the decimal)
print(7 % 2)    # 1    modulo (the remainder)
print(7 ** 2)   # 49   exponent (7 squared)

# Variables can be updated
score = 10
score = score + 5   # now 15
score += 5          # shortcut for score = score + 5, now 20
print("score:", score)

# Converting between types
print(int("42") + 1)    # string -> int: 43
print(str(42) + "!")    # int -> string: "42!"
print(float("3.5"))     # string -> float: 3.5

# Getting input from the user (uncomment the next two lines to try it)
# your_name = input("What's your name? ")
# print("Hello,", your_name)

# ---------------------------------------------------------------
# EXERCISES: replace each `pass` with your code
# ---------------------------------------------------------------


def make_greeting():
    # TODO: create a variable `city` set to "Paris", then return it.
    pass


def total_cost():
    # TODO: an apple costs 3 and you buy 4 of them. Store the price and the
    # count in two variables, then return price times count.
    pass


def remainder_of_17_divided_by_5():
    # TODO: use the % operator to return the remainder of 17 / 5.
    pass


def text_to_number():
    # TODO: the variable below holds TEXT, not a number.
    # Convert it to an int, add 10, and return the result (should be 35).
    text = "25"
    pass


def is_adult(age):
    # TODO: return True if age is 18 or more, otherwise False.
    # Hint: a comparison like `age >= 18` already IS True or False.
    pass


# ---------------------------------------------------------------
# CHECKS: run the file to see if your answers are right
# ---------------------------------------------------------------
print("\n=== Checks ===")
check("make_greeting returns 'Paris'", lambda: make_greeting(), "Paris")
check("total_cost returns 12", lambda: total_cost(), 12)
check("remainder is 2", lambda: remainder_of_17_divided_by_5(), 2)
check("text_to_number returns 35", lambda: text_to_number(), 35)
check("is_adult(20) is True", lambda: is_adult(20), True)
check("is_adult(12) is False", lambda: is_adult(12), False)
summary()
