# Module 05.2 — Collections: Tuples

# Exercise 46 - Tuple Basics
person = ("Alex", 30, "Warsaw", "Developer")
person[0]
# 'Alex'
person[-1]
# 'Developer'
person[1:3]
# (30, 'Warsaw')
"Warsaw" in person
# True
person[1] = 60
# Traceback (most recent call last):
#   File "<python-input-286>", line 1, in <module>
#     person[1] = 60
#     ~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

# Exercise 47 - Tuple Unpacking
coordinates = (52.2297, 21.0122)
latitude, longitude = coordinates
print(latitude)
# 52.2297
print(longitude)
# 21.0122
person = ('Alex', 30, 'Warsaw')
name, age, city = person
print(name, age, city)
# Alex 30 Warsaw

# Exercise 48 - Returning Multiple Values
# first approach
def calculate_stats(numbers):
    def calculate_smallest():
        smallest = numbers[0]
        for num in numbers:
            if num < smallest:
                smallest = num
        return smallest

    def calculate_largest():
        largest = numbers[0]
        for num in numbers:
            if num > largest:
                largest = num
        return largest

    def calculate_total():
        total = 0
        for num in numbers:
            total += num
        return total

    return (
        calculate_smallest(),
        calculate_largest(),
        calculate_total()
    )

# second approach
def calculate_stats(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    total = 0
    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
        total += num

    return (smallest, largest, total)

# Why tuple is a good choice:
# - ordered: order of results matters. Min, max, sum.
# - immutable: returned results set should not be accidently modified.
# - duplicates allowed: different stats can have identical values
