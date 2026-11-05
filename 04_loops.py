"""
LESSON 4: Loops (repeating things)
==================================
`for` loops go through each item in a sequence.
`while` loops keep going as long as a condition is True.

Run this file:  python 04_loops.py
"""
from checker import check, summary

# ---------------------------------------------------------------
# EXAMPLES
# ---------------------------------------------------------------
print("=== Examples ===")

# range(5) gives 0, 1, 2, 3, 4 (stops BEFORE 5)
for i in range(5):
    print("i is", i)

# range(start, stop, step)
for n in range(2, 11, 2):
    print(n, end=" ")      # end=" " keeps printing on the same line
print()                    # print a newline

# Loop over a string, one character at a time
for letter in "hey":
    print(letter)

# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)

# enumerate gives you the position AND the item
for index, fruit in enumerate(fruits):
    print(index, fruit)

# The "accumulator" pattern: start with a value, build it up in a loop
total = 0
for n in range(1, 4):
    total += n         # 1, then 3, then 6
print("total:", total)

# while loop
countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1     # don't forget this, or the loop never ends!
print("Liftoff!")

# break exits the loop early; continue skips to the next round
for n in range(10):
    if n == 2:
        continue       # skip 2
    if n == 5:
        break          # stop entirely at 5
    print(n, end=" ")  # prints 0 1 3 4
print()

# Nested loops
for row in range(1, 4):
    for col in range(1, 4):
        print(row * col, end="\t")
    print()

# ---------------------------------------------------------------
# EXERCISES
# ---------------------------------------------------------------


def sum_to(n):
    # TODO: return 1 + 2 + ... + n using a loop. sum_to(4) -> 10
    pass


def count_vowels(text):
    # TODO: return how many vowels (a, e, i, o, u) are in text.
    # Hint: loop over each letter, and check `if letter in "aeiou"`.
    pass


def factorial(n):
    # TODO: return n! = 1 * 2 * 3 * ... * n. factorial(5) -> 120
    # factorial(0) should be 1.
    pass


def multiples_of(k, limit):
    # TODO: return a list of all multiples of k from k up to limit (inclusive).
    # multiples_of(3, 10) -> [3, 6, 9]
    # Hint: start with result = [] and use result.append(x) inside the loop.
    pass


def first_over(numbers, threshold):
    # TODO: return the first number in the list that is bigger than threshold.
    # If none are, return None. Try using `break` or an early `return`.
    pass


def halvings(n):
    # TODO: using a WHILE loop, count how many times you can divide n by 2
    # (using //) before it reaches 1. halvings(8) -> 3  (8 -> 4 -> 2 -> 1)
    pass


# ---------------------------------------------------------------
# CHECKS
# ---------------------------------------------------------------
print("\n=== Checks ===")
check("sum_to(4)", lambda: sum_to(4), 10)
check("sum_to(100)", lambda: sum_to(100), 5050)
check("count_vowels('programming')", lambda: count_vowels("programming"), 3)
check("factorial(5)", lambda: factorial(5), 120)
check("factorial(0)", lambda: factorial(0), 1)
check("multiples_of(3, 10)", lambda: multiples_of(3, 10), [3, 6, 9])
check("first_over([1, 5, 8, 12], 6)", lambda: first_over([1, 5, 8, 12], 6), 8)
check("first_over([1, 2], 6)", lambda: first_over([1, 2], 6), None)
check("halvings(8)", lambda: halvings(8), 3)
check("halvings(1)", lambda: halvings(1), 0)
summary()
