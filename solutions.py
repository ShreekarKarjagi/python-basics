"""
SOLUTIONS - try the exercises yourself first!
=============================================
There is usually more than one correct answer. If yours passes the checks,
it's right, even if it looks different from these.

Run this file to confirm every solution passes:  python solutions.py
"""
import random

from checker import check, summary

# ---------------- Lesson 1: Variables and Types ----------------


def make_greeting():
    city = "Paris"
    return city


def total_cost():
    price = 3
    count = 4
    return price * count


def remainder_of_17_divided_by_5():
    return 17 % 5


def text_to_number():
    text = "25"
    return int(text) + 10


def is_adult(age):
    return age >= 18


# ---------------- Lesson 2: Strings ----------------


def shout(text):
    return text.upper() + "!"


def first_and_last(text):
    return text[0] + text[-1]


def reverse(text):
    return text[::-1]


def introduce(name, age):
    return f"My name is {name} and I am {age}."


def count_words(sentence):
    return len(sentence.split())


def is_palindrome(text):
    lowered = text.lower()
    return lowered == lowered[::-1]


# ---------------- Lesson 3: Conditionals ----------------


def sign(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"


def is_even(n):
    return n % 2 == 0


def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def fizzbuzz(n):
    # "Both" must come first: 15 is divisible by 3, so checking 3 first
    # would return "Fizz" and never reach the FizzBuzz case.
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def can_ride(height_cm, with_adult):
    return height_cm >= 140 or (height_cm >= 120 and with_adult)


# ---------------- Lesson 4: Loops ----------------


def sum_to(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def count_vowels(text):
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def multiples_of(k, limit):
    result = []
    for x in range(k, limit + 1, k):
        result.append(x)
    return result


def first_over(numbers, threshold):
    for n in numbers:
        if n > threshold:
            return n
    return None


def halvings(n):
    count = 0
    while n > 1:
        n //= 2
        count += 1
    return count


# ---------------- Lesson 5: Functions ----------------


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def average(numbers):
    return sum(numbers) / len(numbers)


def power(base, exponent=2):
    return base ** exponent


def describe_number(n):
    kind = "even" if n % 2 == 0 else "odd"
    return f"{n} is {kind}"


def largest(numbers):
    biggest = numbers[0]          # start with the first, not 0 (negatives!)
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest


# ---------------- Lesson 6: Collections ----------------


def double_all(numbers):
    return [n * 2 for n in numbers]


def only_positive(numbers):
    return [n for n in numbers if n > 0]


def remove_duplicates(items):
    return sorted(set(items))


def word_counts(sentence):
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def phone_lookup(phonebook, name):
    return phonebook.get(name, "unknown")


def oldest_person(people):
    oldest_name = None
    oldest_age = -1
    for name, age in people.items():
        if age > oldest_age:
            oldest_name, oldest_age = name, age
    return oldest_name
    # Shorter alternative: return max(people, key=people.get)


# ---------------- Lesson 7: Classes ----------------


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False


# ---------------- Lesson 8: Mini Project ----------------


def get_guess():
    while True:
        text = input("Your guess: ")
        try:
            return int(text)
        except ValueError:
            print("Please type a whole number.")


def check_guess(guess, secret):
    if guess > secret:
        return "high"
    elif guess < secret:
        return "low"
    return "correct"


def play():
    secret = random.randint(1, 100)
    attempts = 0
    print("I'm thinking of a number between 1 and 100.")
    while True:
        guess = get_guess()
        attempts += 1
        result = check_guess(guess, secret)
        if result == "high":
            print("Too high!")
        elif result == "low":
            print("Too low!")
        else:
            print(f"You got it in {attempts} guesses!")
            break


# ---------------- Check every solution ----------------
if __name__ == "__main__":
    check("L1 make_greeting", make_greeting, "Paris")
    check("L1 total_cost", total_cost, 12)
    check("L1 remainder", remainder_of_17_divided_by_5, 2)
    check("L1 text_to_number", text_to_number, 35)
    check("L1 is_adult", lambda: (is_adult(20), is_adult(12)), (True, False))
    check("L2 shout", lambda: shout("hi"), "HI!")
    check("L2 first_and_last", lambda: first_and_last("hello"), "ho")
    check("L2 reverse", lambda: reverse("abc"), "cba")
    check("L2 introduce", lambda: introduce("Sam", 19), "My name is Sam and I am 19.")
    check("L2 count_words", lambda: count_words("the quick brown fox"), 4)
    check("L2 is_palindrome", lambda: (is_palindrome("Racecar"), is_palindrome("Python")), (True, False))
    check("L3 sign", lambda: (sign(5), sign(-3), sign(0)), ("positive", "negative", "zero"))
    check("L3 letter_grade", lambda: [letter_grade(s) for s in (95, 81, 42)], ["A", "B", "F"])
    check("L3 fizzbuzz", lambda: [fizzbuzz(n) for n in (15, 9, 10, 7)], ["FizzBuzz", "Fizz", "Buzz", "7"])
    check("L3 can_ride", lambda: (can_ride(150, False), can_ride(125, True), can_ride(125, False)), (True, True, False))
    check("L4 sum_to", lambda: sum_to(100), 5050)
    check("L4 count_vowels", lambda: count_vowels("programming"), 3)
    check("L4 factorial", lambda: (factorial(5), factorial(0)), (120, 1))
    check("L4 multiples_of", lambda: multiples_of(3, 10), [3, 6, 9])
    check("L4 first_over", lambda: (first_over([1, 5, 8, 12], 6), first_over([1, 2], 6)), (8, None))
    check("L4 halvings", lambda: (halvings(8), halvings(1)), (3, 0))
    check("L5 celsius_to_fahrenheit", lambda: celsius_to_fahrenheit(100), 212.0)
    check("L5 average", lambda: average([2, 4, 6]), 4.0)
    check("L5 power", lambda: (power(3), power(2, 5)), (9, 32))
    check("L5 describe_number", lambda: describe_number(7), "7 is odd")
    check("L5 largest", lambda: (largest([3, 9, 2, 7]), largest([-5, -2, -8])), (9, -2))
    check("L6 double_all", lambda: double_all([1, 2, 3]), [2, 4, 6])
    check("L6 only_positive", lambda: only_positive([-1, 4, 0, 7]), [4, 7])
    check("L6 remove_duplicates", lambda: remove_duplicates([3, 1, 3, 2, 1]), [1, 2, 3])
    check("L6 word_counts", lambda: word_counts("the cat the hat"), {"the": 2, "cat": 1, "hat": 1})
    check("L6 phone_lookup", lambda: phone_lookup({"sam": "1"}, "max"), "unknown")
    check("L6 oldest_person", lambda: oldest_person({"a": 20, "b": 40, "c": 30}), "b")
    check("L7 Rectangle", lambda: (Rectangle(3, 4).area(), Rectangle(3, 4).perimeter()), (12, 14))
    check("L8 check_guess", lambda: [check_guess(g, 50) for g in (70, 20, 50)], ["high", "low", "correct"])
    summary()
