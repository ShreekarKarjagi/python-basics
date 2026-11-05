"""
LESSON 7: Classes and Objects
=============================
A class is a blueprint. An object is a thing built from that blueprint.
Objects bundle DATA (attributes) and BEHAVIOR (methods) together.

Example: the class `Dog` describes what every dog has (a name) and can do
(bark). `rex = Dog("Rex")` creates one specific dog.

Run this file:  python 07_classes.py
"""
from checker import check, summary

# ---------------------------------------------------------------
# EXAMPLES
# ---------------------------------------------------------------
print("=== Examples ===")


class Dog:
    # __init__ runs automatically when you create a new Dog.
    # `self` means "this particular object".
    def __init__(self, name, age):
        self.name = name     # attributes: data stored on the object
        self.age = age
        self.tricks = []

    # Methods are functions that belong to the class. They always take self.
    def bark(self):
        return f"{self.name} says woof!"

    def learn(self, trick):
        self.tricks.append(trick)

    def birthday(self):
        self.age += 1


rex = Dog("Rex", 3)
fido = Dog("Fido", 5)     # a separate dog with its own data

print(rex.bark())
print(fido.name, fido.age)
rex.learn("sit")
rex.birthday()
print(rex.name, rex.age, rex.tricks)
print(fido.tricks)        # [] - Fido didn't learn anything


# Inheritance: a new class can build on an existing one
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def introduce(self):
        return f"I am {self.name} and I say {self.speak()}"


class Cat(Animal):        # Cat inherits everything from Animal
    def speak(self):      # ...but overrides speak()
        return "meow"


print(Cat("Tom").introduce())   # I am Tom and I say meow

# ---------------------------------------------------------------
# EXERCISES: fill in the methods of these classes
# ---------------------------------------------------------------


class Rectangle:
    def __init__(self, width, height):
        # TODO: store width and height on self
        pass

    def area(self):
        # TODO: return width * height
        pass

    def perimeter(self):
        # TODO: return 2 * (width + height)
        pass

    def is_square(self):
        # TODO: return True if width equals height
        pass


class BankAccount:
    def __init__(self, owner, balance=0):
        # TODO: store owner and balance on self
        pass

    def deposit(self, amount):
        # TODO: add amount to the balance
        pass

    def withdraw(self, amount):
        # TODO: if there's enough money, subtract amount and return True.
        # Otherwise, leave the balance alone and return False.
        pass


# ---------------------------------------------------------------
# CHECKS
# ---------------------------------------------------------------
print("\n=== Checks ===")
check("Rectangle(3, 4).area()", lambda: Rectangle(3, 4).area(), 12)
check("Rectangle(3, 4).perimeter()", lambda: Rectangle(3, 4).perimeter(), 14)
check("Rectangle(5, 5).is_square()", lambda: Rectangle(5, 5).is_square(), True)
check("Rectangle(2, 5).is_square()", lambda: Rectangle(2, 5).is_square(), False)


def bank_test():
    acct = BankAccount("Jo", 100)
    acct.deposit(50)
    ok = acct.withdraw(30)
    too_much = acct.withdraw(1000)
    return acct.owner, acct.balance, ok, too_much


check("BankAccount deposit/withdraw", bank_test, ("Jo", 120, True, False))
check("BankAccount default balance", lambda: BankAccount("Al").balance, 0)
summary()
