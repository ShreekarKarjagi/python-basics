"""
LESSON 3: Conditionals (making decisions)
=========================================
`if` runs code only when a condition is True. The code inside must be
indented (4 spaces). `elif` means "else if". `else` catches everything else.

Run this file:  python 03_conditionals.py
"""
from checker import check, summary

# ---------------------------------------------------------------
# EXAMPLES
# ---------------------------------------------------------------
print("=== Examples ===")

temperature = 25

if temperature > 30:
    print("It's hot")
elif temperature > 15:
    print("It's nice")     # this one runs
else:
    print("It's cold")

# Comparison operators (each gives True or False)
#   ==  equal          !=  not equal
#   <   less than      >   greater than
#   <=  less or equal  >=  greater or equal
print(5 == 5, 5 != 3, 2 < 1)    # True True False

# NOTE: `=` assigns a value, `==` compares two values. Easy to mix up!

# Logic operators: and, or, not
age, has_ticket = 20, True
if age >= 18 and has_ticket:
    print("You can enter")
if not has_ticket:
    print("This won't print")
if age < 13 or age > 65:
    print("Discount!")
else:
    print("Full price")

# "Truthy" and "falsy": 0, "", [], and None count as False in an if
items = []
if not items:
    print("The list is empty")

# One-line if (conditional expression)
label = "even" if 10 % 2 == 0 else "odd"
print(label)

# ---------------------------------------------------------------
# EXERCISES
# ---------------------------------------------------------------


def sign(n):
    # TODO: return "positive" if n > 0, "negative" if n < 0, or "zero".
    pass


def is_even(n):
    # TODO: return True if n is even. Hint: even numbers have n % 2 == 0.
    pass


def letter_grade(score):
    # TODO: return the letter grade for a score from 0 to 100:
    #   90 and up -> "A", 80-89 -> "B", 70-79 -> "C", 60-69 -> "D", below 60 -> "F"
    pass


def fizzbuzz(n):
    # TODO: classic interview question!
    #   if n is divisible by both 3 and 5 -> return "FizzBuzz"
    #   if divisible by 3 only            -> return "Fizz"
    #   if divisible by 5 only            -> return "Buzz"
    #   otherwise                         -> return n as a string, e.g. "7"
    # Hint: check the "both" case FIRST. Why does order matter?
    pass


def can_ride(height_cm, with_adult):
    # TODO: a rider can go on the rollercoaster if they are at least 140 cm
    # tall, OR at least 120 cm tall AND riding with an adult.
    pass


# ---------------------------------------------------------------
# CHECKS
# ---------------------------------------------------------------
print("\n=== Checks ===")
check("sign(5)", lambda: sign(5), "positive")
check("sign(-3)", lambda: sign(-3), "negative")
check("sign(0)", lambda: sign(0), "zero")
check("is_even(4)", lambda: is_even(4), True)
check("is_even(7)", lambda: is_even(7), False)
check("letter_grade(95)", lambda: letter_grade(95), "A")
check("letter_grade(81)", lambda: letter_grade(81), "B")
check("letter_grade(42)", lambda: letter_grade(42), "F")
check("fizzbuzz(15)", lambda: fizzbuzz(15), "FizzBuzz")
check("fizzbuzz(9)", lambda: fizzbuzz(9), "Fizz")
check("fizzbuzz(10)", lambda: fizzbuzz(10), "Buzz")
check("fizzbuzz(7)", lambda: fizzbuzz(7), "7")
check("can_ride(150, False)", lambda: can_ride(150, False), True)
check("can_ride(125, True)", lambda: can_ride(125, True), True)
check("can_ride(125, False)", lambda: can_ride(125, False), False)
summary()
