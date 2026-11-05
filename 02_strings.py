"""
LESSON 2: Strings
=================
Strings are text. You can combine them, slice them, and use built-in
methods to transform them.

Run this file:  python 02_strings.py
"""
from checker import check, summary

# ---------------------------------------------------------------
# EXAMPLES
# ---------------------------------------------------------------
print("=== Examples ===")

word = "Python"

# Joining strings
print("Hello, " + word)       # concatenation with +
print(word * 3)               # repetition: PythonPythonPython

# f-strings: put variables inside {} (note the f before the quote)
lang, year = "Python", 1991
print(f"{lang} was released in {year}.")
print(f"2 + 3 = {2 + 3}")     # you can put expressions inside {}

# Length
print(len(word))              # 6

# Indexing: positions start at 0
#   P  y  t  h  o  n
#   0  1  2  3  4  5
#  -6 -5 -4 -3 -2 -1
print(word[0])     # P
print(word[-1])    # n (negative counts from the end)

# Slicing: word[start:stop] gives characters from start up to (not including) stop
print(word[0:3])   # Pyt
print(word[2:])    # thon  (to the end)
print(word[:2])    # Py    (from the start)
print(word[::-1])  # nohtyP (reversed)

# Common methods
msg = "  Hello World  "
print(msg.upper())          # "  HELLO WORLD  "
print(msg.lower())          # "  hello world  "
print(msg.strip())          # "Hello World" (removes outer spaces)
print(msg.replace("World", "There"))
print("a,b,c".split(","))   # ['a', 'b', 'c']
print("-".join(["a", "b", "c"]))  # "a-b-c"
print("World" in msg)       # True (checks if text is inside)
print(msg.strip().startswith("Hello"))  # True

# ---------------------------------------------------------------
# EXERCISES
# ---------------------------------------------------------------


def shout(text):
    # TODO: return text in all capital letters with "!" on the end.
    # shout("hi") -> "HI!"
    pass


def first_and_last(text):
    # TODO: return a string made of the first and last character.
    # first_and_last("hello") -> "ho"
    pass


def reverse(text):
    # TODO: return the text reversed. reverse("abc") -> "cba"
    pass


def introduce(name, age):
    # TODO: use an f-string to return "My name is <name> and I am <age>."
    # introduce("Sam", 19) -> "My name is Sam and I am 19."
    pass


def count_words(sentence):
    # TODO: return how many words are in the sentence.
    # Hint: .split() with no argument splits on spaces. Then use len().
    pass


def is_palindrome(text):
    # TODO: return True if text reads the same forwards and backwards,
    # ignoring upper/lower case. is_palindrome("Racecar") -> True
    pass


# ---------------------------------------------------------------
# CHECKS
# ---------------------------------------------------------------
print("\n=== Checks ===")
check("shout('hi')", lambda: shout("hi"), "HI!")
check("first_and_last('hello')", lambda: first_and_last("hello"), "ho")
check("reverse('abc')", lambda: reverse("abc"), "cba")
check("introduce('Sam', 19)", lambda: introduce("Sam", 19), "My name is Sam and I am 19.")
check("count_words('the quick brown fox')", lambda: count_words("the quick brown fox"), 4)
check("is_palindrome('Racecar')", lambda: is_palindrome("Racecar"), True)
check("is_palindrome('Python')", lambda: is_palindrome("Python"), False)
summary()
