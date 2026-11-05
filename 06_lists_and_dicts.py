"""
LESSON 6: Collections (lists, tuples, dictionaries, sets)
=========================================================
Collections hold many values in one variable.

  list   [1, 2, 3]          ordered, changeable
  tuple  (1, 2, 3)          ordered, NOT changeable
  dict   {"a": 1, "b": 2}   key -> value lookups
  set    {1, 2, 3}          unordered, no duplicates

Run this file:  python 06_lists_and_dicts.py
"""
from checker import check, summary

# ---------------------------------------------------------------
# EXAMPLES: LISTS
# ---------------------------------------------------------------
print("=== List examples ===")

nums = [5, 3, 8]
nums.append(1)          # add to end         -> [5, 3, 8, 1]
nums.insert(0, 10)      # insert at index 0  -> [10, 5, 3, 8, 1]
nums.remove(3)          # remove first 3     -> [10, 5, 8, 1]
last = nums.pop()       # remove & return last item (1)
print(nums, "popped:", last)

print(nums[0], nums[-1], nums[1:])   # indexing and slicing work like strings
nums[0] = 99                          # lists can be changed in place
print(len(nums), sum(nums), min(nums), max(nums))
print(sorted(nums))                   # a new sorted list
print(8 in nums)                      # True

# List comprehension: build a list in one line
squares = [x * x for x in range(5)]           # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
print(squares, evens)

# ---------------------------------------------------------------
# EXAMPLES: TUPLES
# ---------------------------------------------------------------
print("\n=== Tuple examples ===")
point = (3, 4)
x, y = point          # "unpacking"
print(x, y)
# point[0] = 5        # <- would crash: tuples can't be changed

# ---------------------------------------------------------------
# EXAMPLES: DICTIONARIES
# ---------------------------------------------------------------
print("\n=== Dict examples ===")

ages = {"alice": 30, "bob": 25}
print(ages["alice"])            # look up by key: 30
ages["carol"] = 35              # add a new key
ages["bob"] = 26                # update a value
del ages["alice"]               # remove a key
print(ages)
print("bob" in ages)            # check if a KEY exists: True
print(ages.get("zed", 0))       # get with a default if missing: 0

for name, age in ages.items():  # loop over keys and values
    print(f"{name} is {age}")
print(list(ages.keys()), list(ages.values()))

# ---------------------------------------------------------------
# EXAMPLES: SETS
# ---------------------------------------------------------------
print("\n=== Set examples ===")
colors = {"red", "blue", "red"}   # duplicates disappear
colors.add("green")
print(len(colors))                # 3
a, b = {1, 2, 3}, {2, 3, 4}
print(a & b, a | b, a - b)        # intersection, union, difference

# ---------------------------------------------------------------
# EXERCISES
# ---------------------------------------------------------------


def double_all(numbers):
    # TODO: return a NEW list with every number doubled.
    # double_all([1, 2, 3]) -> [2, 4, 6]   (try a list comprehension!)
    pass


def only_positive(numbers):
    # TODO: return a list with only the numbers greater than 0.
    pass


def remove_duplicates(items):
    # TODO: return a sorted list of the unique items.
    # remove_duplicates([3, 1, 3, 2, 1]) -> [1, 2, 3]   Hint: set() and sorted()
    pass


def word_counts(sentence):
    # TODO: return a dict mapping each word to how many times it appears.
    # word_counts("a b a") -> {"a": 2, "b": 1}
    # Hint: start with counts = {}, loop over the words, and use
    #       counts[word] = counts.get(word, 0) + 1
    pass


def phone_lookup(phonebook, name):
    # TODO: phonebook is a dict like {"sam": "555-1234"}.
    # Return the number for name, or "unknown" if the name isn't in it.
    pass


def oldest_person(people):
    # TODO: people is a dict of name -> age. Return the NAME of the oldest.
    # oldest_person({"a": 20, "b": 40, "c": 30}) -> "b"
    pass


# ---------------------------------------------------------------
# CHECKS
# ---------------------------------------------------------------
print("\n=== Checks ===")
check("double_all([1, 2, 3])", lambda: double_all([1, 2, 3]), [2, 4, 6])
check("only_positive([-1, 4, 0, 7])", lambda: only_positive([-1, 4, 0, 7]), [4, 7])
check("remove_duplicates([3, 1, 3, 2, 1])", lambda: remove_duplicates([3, 1, 3, 2, 1]), [1, 2, 3])
check("word_counts('the cat the hat')", lambda: word_counts("the cat the hat"), {"the": 2, "cat": 1, "hat": 1})
check("phone_lookup found", lambda: phone_lookup({"sam": "555-1234"}, "sam"), "555-1234")
check("phone_lookup missing", lambda: phone_lookup({"sam": "555-1234"}, "max"), "unknown")
check("oldest_person", lambda: oldest_person({"a": 20, "b": 40, "c": 30}), "b")
summary()
