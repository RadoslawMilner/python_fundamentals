# Module 07.2 — Generators

# INTRO:
def generate_numbers():
    yield 10
    yield 20
    yield 30

numbers = generate_numbers()
type(numbers)
# <class 'generator'>
def some_function():
    return 'a'

some_variable = some_function()
some_variable
# 'a'
type(some_variable)
# <class 'str'>
def some_function():
    return 23

some_variable = some_function()
type(some_variable)
# <class 'int'>
def generator():
    yield ''

some_generator = generator()
type(some_generator)
# <class 'generator'>
next(numbers)
# 10
next(numbers)
# 20
next(numbers)
# 30
next(numbers)
# Traceback (most recent call last):
#   File "<python-input-94>", line 1, in <module>
#     next(numbers)
#     ~~~~^^^^^^^^^
# StopIteration
# >>> next(numbers)
# Traceback (most recent call last):
#   File "<python-input-95>", line 1, in <module>
#     next(numbers)
#     ~~~~^^^^^^^^^
# StopIteration

# Exercise 82 - Generator vs ordinary function
def get_numbers(limit):
    return list(range(1, limit + 1))

def generate_numbers(limit):
    for num in range(1, limit + 1):
        yield num

get_numbers(5)
# [1, 2, 3, 4, 5]
generate_numbers(5)
# <generator object generate_numbers at 0x1035bfbc0>
# Różnica:
# - get_numbers(5) natychmiast tworzy listę pięciu elementów.
# - generate_numbers(5) tworzy generator. Liczby będą produkowane dopiero na żądanie.

type(get_numbers(5))
# <class 'list'>
type(generate_numbers(5))
# <class 'generator'>
[get_numbers(5)]
# [[1, 2, 3, 4, 5]]
generated_numbers = generate_numbers(5)
next([generated_numbers])
# Traceback (most recent call last):
#   File "<python-input-150>", line 1, in <module>
#     next([generated_numbers])
#     ~~~~^^^^^^^^^^^^^^^^^^^^^
# TypeError: 'list' object is not an iterator
# Zwróciło TypeError, ponieważ [generated_numbers] tworzy nową listę zawierającą generator. Lista jest iterable, ale sama nie jest iteratorem.
next(iter([generated_numbers]))
# To zwróci obiekt generatora jako pierwszy element listy, a nie pierwszą liczbę z generatora.

next(generated_numbers)
# 1
next(generated_numbers)
# 2
next(generated_numbers)
# 3
next(generated_numbers)
# 4
next(generated_numbers)
# 5
next(generated_numbers)
# Traceback (most recent call last):
#   File "<python-input-140>", line 1, in <module>
#     next(generated_numbers)
#     ~~~~^^^^^^^^^
# StopIteration

# Exercise 83 - Generator state
def manually_produce_numbers():
    print('first')
    yield 1
    print('second')
    yield 2
    print('third')
    yield 3

manually_produce_numbers()
# <generator object manually_produce_numbers at 0x1034f3640>
generator_v = manually_produce_numbers()
# tworzy jeden konkretny generator, którego stan jest zachowywany pomiędzy wywołaniami next().
generator_v
# <generator object manually_produce_numbers at 0x103630280>
type(generator_v)
# <class 'generator'>
next(manually_produce_numbers())
# first
# 1
next(manually_produce_numbers())
# first
# 1
next(manually_produce_numbers())
# first
# 1
next(manually_produce_numbers())
# first
# 1
# BECAUSE: Za każdym razem, gdy wywołujesz manually_produce_numbers(), tworzysz NOWY GENERATOR. EVERY. SINGLE. TIME.
next(generator_v)
# first
# 1
next(generator_v)
# second
# 2
next(generator_v)
# third
# 3
next(generator_v)
# Traceback (most recent call last):
#   File "<python-input-169>", line 1, in <module>
#     next(generator_v)
#     ~~~~^^^^^^^^^^^^^
# StopIteration

# !!! IMPORTANT
# GENERATOR NIE PRZECHOWUJE GOTOWEJ KOLEKCJI WYNIKÓW. ZACHOWUJE STAN WYKONYWANIA.

# Exercise 84
# generator:
def running_total(numbers):
    current_sum = 0
    for num in numbers:
        current_sum += num
        yield current_sum

# generator call - wywołanie funkcji generatorowej, która tworzy nowy obiekt generatora
running_total(numbers)
# <generator object running_total at 0x1035bfd80>

# function call - referencja do obiektu funkcji
running_total
# <function running_total at 0x1036b4040>

# incorrect generator call due to lack of argument:
running_total()
# Traceback (most recent call last):
#   File "<python-input-184>", line 1, in <module>
#     running_total()
#     ~~~~~~~~~~~~~^^
# TypeError: running_total() missing 1 required positional argument: 'numbers'

# incorrect next call, poniewaz jest stosowane na wywolaniu funkcji. a ta w przeciwienstwie do generatora nie jest iteratorem.
next(running_total)
# Traceback (most recent call last):
#   File "<python-input-185>", line 1, in <module>
#     next(running_total)
#     ~~~~^^^^^^^^^^^^^^^
# TypeError: 'function' object is not an iterator

# incorrect next call, poniewaz przekazany generator nie ma przekazanego argumentu
next(running_total())
# Traceback (most recent call last):
#   File "<python-input-186>", line 1, in <module>
#     next(running_total())
#          ~~~~~~~~~~~~~^^
# TypeError: running_total() missing 1 required positional argument: 'numbers'

# soft-incorrect next call, poniewaz za kazdym razem tworzymy nowy generator. wiec zaczyna zawsze od poczatku.
next(running_total(numbers))
# 10
next(running_total(numbers))
# 10
next(running_total(numbers))
# 10

# incorrect assigning expression / next call function to variable
# przypisujemy wynik pierwszego next(), czyli int o wartości 10, a nie generator.
# Dlatego późniejsze next(generator_running_total_numbers) kończy się TypeError.
generator_running_total_numbers = next(running_total(numbers))
next(generator_running_total_numbers)
# Traceback (most recent call last):
#   File "<python-input-191>", line 1, in <module>
#     next(generator_running_total_numbers)
#     ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: 'int' object is not an iterator

# correct assigning generator to variable. now variable is iterator
generator_running_total_numbers = running_total(numbers)
# thus we can iterate over this new iterator
next(generator_running_total_numbers)
# 10
next(generator_running_total_numbers)
# 30
next(generator_running_total_numbers)
# 60
next(generator_running_total_numbers)
# 100

# till to it is exhausted
next(generator_running_total_numbers)
# Traceback (most recent call last):
#   File "<python-input-205>", line 1, in <module>
#     next(generator_running_total_numbers)
#     ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# StopIteration

# Answer: poniewaz nie wywolujemy calej funkcji od nowa za kazdym razem. uzywamy funkcji next na iteratorze, to return 'next' item from the iterator. ponadto iterator utrzymuje stan w pamieci.
# Kiedy generator napotyka yield, zawiesza wykonanie. Python zachowuje m.in.:
# - aktualne miejsce wykonania funkcji,
# - lokalne zmienne,
# - stan iteracji,
# - kontekst potrzebny do wznowienia wykonania.
# Dlatego current_sum nie jest inicjalizowane ponownie przy każdym next(). generator zachowuje kontekst pomiędzy kolejnymi wywołaniami.

# Exercise 85 — Lazy evaluation w praktyce
records = [100, 200, 300, 400, 500]
def process_all(records):
    return [num * 2 for num in records]

def process_one_by_one(records):
    for num in records:
        yield num * 2

type(process_all(records))
# <class 'list'>
type(process_one_by_one(records))
# <class 'generator'>
processed_records = process_one_by_one(records)
next(processed_records)
# 200
# 'Sprawdź, czy pozostałe elementy zostały już przetworzone.' -> aby sprawdzic pozostałe/kolejne elementy, nalezy kolejno wywoływać do skutku/do StopIteration error.
# Poniewaz generator zawiesza wykonanie wraz z yield. Wiec kolejne elementy nie zostana przetworzone, do momentu kolejnego zadania ich generacji-produkcji.
next(processed_records)
# 400

# IMPORTANT: lista records już istnieje w pamięci. Generator nie sprawia, że dane wejściowe przestają zajmować pamięć.
# Oszczędność dotyczy przede wszystkim kolekcji wynikowej.
# Przy 10 milionach rekordów:
# - lista wynikowa musi przechowywać 10 milionów wartości;
# - generator może produkować wartości pojedynczo, bez tworzenia drugiej, ogromnej kolekcji.
# Oczywiście generator może również przetwarzać dane wejściowe pochodzące ze strumienia lub pliku, bez wcześniejszego ładowania całego zbioru do pamięci.

# Exercise 86 - Generator pipeline
records = [100, 200, 300, 400, 500]
def double(numbers):
    for num in numbers:
        yield num * 2
    
def filter_large(numbers):
    for num in numbers:
        if num > 500:
            yield num
    
def add_tax(numbers):
    for num in numbers:
        yield num * 1.23

result = add_tax(filter_large(double(records)))
next(result)
# 738.0
next(result)
# 984.0
next(result)
# 1230.0
next(result)
# Traceback (most recent call last):
#   File "<python-input-5>", line 1, in <module>
#     next(result)
#     ~~~~^^^^^^^^
# StopIteration

# answer to bonus question: Suspends the execution of a specific generator while preserving its state.

# Exercise 87: Generator Expressions
numbers = [2, 5, 8, 11, 14, 17, 20]
even_squares = (num ** 2 for num in numbers if num % 2 == 0)
type(even_squares)
# <class 'generator'>
next(even_squares)
# 4
next(even_squares)
# 64
for num in even_squares:
    print(num)
# 196
# 400
next(even_squares)
# Traceback (most recent call last):
#   File "<python-input-27>", line 1, in <module>
#     next(even_squares)
#     ~~~~^^^^^^^^^^^^^^
# StopIteration


# Generator expression vs Generator function:

# Krótka składnia	                            | Pełna definicja funkcji
# Dobra do prostych transformacji i filtracji |	Dobra do bardziej złożonej logiki
# Nie wymaga yield	                          | Wymaga yield
# Jedno wyrażenie	                            | Dowolny blok instrukcji
# Zwraca generator                            | Wywołanie zwraca generator

# Exercise 88 — Generator expression jako argument funkcji
numbers = [12, 5, 18, 7, 24, 3, 30, 9]

# 88.1
sum(num for num in numbers if num % 2 == 0)
# 84

# 88.2
count_above_10 = 0
for num in (num for num in numbers if num > 10):
    count_above_10 += 1

count_above_10
# 4

# 88.3
max(num ** 2 for num in numbers if num % 2 != 0)
# 81

# 88.4
sum(num for num in numbers if num >= 10) / sum(
    1 for _ in numbers if _ >= 10
)
# 21.0

# sum() przechodzi przez generator i konsumuje wszystkie jego wartości.
# dlatego:
squares = (num ** 2 for num in numbers)
squares
# <generator object <genexpr> at 0x10499f2a0>
sum(squares)
# 2108
sum(squares)
# 0
total = sum(squares)
total
# 0
# i tym dalej:
largest = max(squares)
# Traceback (most recent call last):
#   File "<python-input-114>", line 1, in <module>
#     largest = max(squares)
# ValueError: max() iterable argument is empty

# Exercise 89 — eksperyment z wyczerpywaniem generatora
numbers = [2, 4, 6, 8]
squares = (num ** 2 for num in numbers)
squares
# <generator object <genexpr> at 0x104aaca00>
next(squares)
# 4
sum(squares)
# IMPORTANT !!! Pierwsza wartość (4) została wcześniej pobrana przez next(), więc sum() jej już nie uwzględnił.
# 116
list(squares)
# []
next(squares)
# Traceback (most recent call last):
#   File "<python-input-122>", line 1, in <module>
#     next(squares)
#     ~~~~^^^^^^^^^
# StopIteration

# stan generatora sie wyczerpal. funkcja sum wyczerpala iterator
second_squares = (num ** 2 for num in numbers)
max(second_squares)
# 64
sum(second_squares)
# 0
# Moge uzyc max przed sum. lecz po max iterator jest wyczerpany. poniewaz max musi pobrac wszystkie rekordy, aby stwierdzic czy dana wartosc jest maksymalna.

# teraz rozumiem

# Exercise 90 — Integracja: generator pipeline
transactions = [
    {"id": 1, "amount": 120.50, "status": "completed"},
    {"id": 2, "amount": 80.00, "status": "pending"},
    {"id": 3, "amount": 250.00, "status": "completed"},
    {"id": 4, "amount": 45.00, "status": "failed"},
    {"id": 5, "amount": 310.00, "status": "completed"},
    {"id": 6, "amount": 175.00, "status": "completed"},
    {"id": 7, "amount": 60.00, "status": "pending"},
]

# tak, sorry. literówki. poprawione.
def completed(transactions):
    for t in transactions:
        if t['status'] == 'completed':
            yield t

def above_100(transactions):
    for t in transactions:
        if t['amount'] >= 100:
            yield t

def taxed(transactions):
    for t in transactions:
        yield dict(id = t['id'], amount = t['amount'], amount_with_tax = t['amount'] * 1.23)

filtered_ts = taxed(above_100(completed(transactions)))
qualifying_transactions_count = 0
amount_sum_before_tax = 0
amount_sum_after_tax = 0
largest_amount_after_tax = 0
for num in filtered_ts:
    qualifying_transactions_count +=1
    amount_sum_before_tax += num['amount']
    amount_sum_after_tax += num['amount_with_tax']
    if num["amount_with_tax"] > largest_amount_after_tax:
        largest_amount_after_tax = num['amount_with_tax']

qualifying_transactions_count
# 4
amount_sum_before_tax
# 855.5
amount_sum_after_tax
# 1052.265
largest_amount_after_tax
# 381.3
