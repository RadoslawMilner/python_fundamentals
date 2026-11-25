# Module 07.1 — Iterators

# Exercise 78 - Basic Iterator
# 78.1
numbers = [10, 20, 30, 40, 50]
iterator = iter(numbers)
# 78.2
next(iterator)
# 10
next(iterator)
# 20
next(iterator)
# 30
# 78.3
for num in iterator:
    print(num)
# 40
# 50
# 78.4
next(iterator)
# Traceback (most recent call last):
#   File "<python-input-32>", line 1, in <module>
#     next(iterator)
#     ~~~~^^^^^^^^^^
# StopIteration
# 78.5
iterator = iter(numbers)
while True:
    try:
        num = next(iterator)
    except StopIteration:
        break
    
    print(num)

# Exercise 79 - Iterator state
words = ["Python", "Ruby", "Java", "Go"]
# 79.1
iterator = iter(words)
# 79.2
next(iterator)
# 'Python'
# 79.3
next(iterator)
# 'Ruby'
# 79.4
for num in iterator:
    print(num)

# Java
# Go
# 79.5
for num in iterator:
    print(num)

# 79.6
iterator = iter(words)
for num in iterator:
    print(num)

# Python
# Ruby
# Java
# Go

# Exercise 80
numbers = [1, 2, 3]
iterator = iter(numbers)
type(numbers)
# <class 'list'>
isinstance(numbers, Iterable)
# Traceback (most recent call last):
#   File "<python-input-54>", line 1, in <module>
#     isinstance(numbers, Iterable)
#                         ^^^^^^^^
# NameError: name 'Iterable' is not defined
from collections.abc import Iterable, Iterator
# 80.1
isinstance(numbers, Iterable)
# True
# 80.2
isinstance(numbers, Iterator)
# False
# 80.3
isinstance(iterator, Iterable)
# True
# 80.4
isinstance(iterator, Iterator)
# True
# Dlaczego iterator jest również iterable?
# Python rozróżnia dwa protokoły:
# 1. Iterable protocol -> Obiekt udostępnia metodę:
# __iter__()
# 2. Iterator protocol ->Obiekt udostępnia obie metody:
# __iter__()
# __next__()
# Istotna zasada: __iter__() iteratora zwraca sam iterator.
iter(iterator) is iterator
# True
# Dlatego iterator spełnia również warunki iterable.
# Natomiast lista ma __iter__(), ale nie implementuje własnego __next__().
# Dopiero iter(numbers) zwraca iterator, który posiada oba mechanizmy.

# Exercise 81
numbers = [10, 20, 30]
iter(numbers) is numbers
# False
# because iterator != iterable. because their protocols differs.
iterator1 = iter(numbers)
iterator2 = iter(numbers)
# the states should be independent
next(iterator1)
# 10
next(iterator2)
# 10
next(iterator2)
# 20
# they are independent:
next(iterator1)
# 20
iter(iterator1) is iterator1
# True
# because iterator is also iterable.
iter(iterator1) is iterator2
# False
# their states are different/independent. both these 2 iterators are two objects. each object should have its own state.
# just as it is wrote in docs and i cant put it in a better way:
# 'A container object (such as a list) produces a fresh new iterator each time you pass it to the iter() function or use it in a for loop'
