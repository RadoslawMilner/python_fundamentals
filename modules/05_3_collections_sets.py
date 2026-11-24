# Module 05.3 — Collections: Sets

# Exercise 49 - Set Basics
numbers = {1, 2, 3, 3, 4, 4, 5}
numbers
# {1, 2, 3, 4, 5}
numbers.add(6)
numbers
# {1, 2, 3, 4, 5, 6}
numbers.update([7, 8, 9])
numbers
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
numbers.remove(3)
numbers
# {1, 2, 4, 5, 6, 7, 8, 9}
numbers.discard(100)
numbers
# {1, 2, 4, 5, 6, 7, 8, 9}
8 in numbers
# True

# Exercise 50 - Set Operations
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
# Union - set sum
a | b
# {1, 2, 3, 4, 5, 6, 7, 8}
# Intersection - all elements from both of sets
a & b
# {4, 5}
# Difference - set difference
a - b
# {1, 2, 3}
b - a
# {8, 6, 7}
# Symetric Difference - elements that appear in only one of the sets
a ^ b
# {1, 2, 3, 6, 7, 8}
# Question: Symetric Difference is the opposite to Intersection?

# Exercise 51 - Remove Duplicates with Set
numbers = []
seen = set()
new_list = []
for num in numbers:
    if num in seen:
        continue
    new_list.append(num)
    seen.add(num)

# te dwa różne zbiory danych pełnią dwie różne funkcje.
# - new_list - Przechowuje wynik i zachowuje kolejność
# - seen - Szybko sprawdza, czy element już wystąpił
# Złożoność:
# - Iteracja: O(n)
# - Sprawdzanie num in seen: średnio O(1)
# - Dodawanie do zbioru: średnio O(1)
# - Całość: średnio O(n)

# Set Question: Why i cannot define set define with just integer.
# # I see that it must be iterable object? But if so, why then I can add just integer, via method: add?
saw_item = set()
saw_item.add(1)
saw_item
# {1}
type({1})
# <class 'set'>
set(1)
# Traceback (most recent call last):
  # File "<python-input-94>", line 1, in <module>
    # set(1)
    # ~~~^^^
# TypeError: 'int' object is not iterable
set([1])
# {1}

# Exercise 52 - Common Elements
users_a = {'alex', 'john', 'maria', 'kate'}
users_b = {'john', 'maria', 'peter', 'sarah'}
# first - its an intersection
users_a & users_b
# {'john', 'maria'}
# second - its a difference
users_a - users_b
# {'alex', 'kate'}

# Exercise 53 - set reinforcement of knowledge
numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]
def unique_values(numbers):
    return set(numbers)

unique_values(numbers)
# {1, 2, 3, 4, 5, 6}
