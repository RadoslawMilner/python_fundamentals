# Module 04.5 - Functions: Scope, Closures & First-Class Functions

# Exercise 37 - Nested Functions
def calculate_order(price, quantity):
    def calculate_subtotal():
        return price * quantity

    def calculate_tax(subtotal):
        return subtotal * 1.23

    return calculate_tax(calculate_subtotal())

calculate_order(100, 2)
# 246.0

# Exercise 38 - LEGB Rule (Code Analysis)
x = 'global'
def outer():
    x = 'enclosing'

    def inner():
        print(x)

    inner()

outer()
# przeanalizowałem kod. zgodnie z załozeniami, print powinien być -> enclosing. sprawdziłem:
outer()
# inner() nie ma lokalnego powiazania nazwy x. Dlatego Python przechodzi do enclosing scope i znajduje x = 'enclosing'

# Exercise 39 - Nonlocal
def create_counter():
    counter = 0
    def increment():
        counter += 1
        return counter
    
    return increment

create_counter()
# <function create_counter.<locals>.increment at 0x1053894e0>
counter = create_counter()
counter()
# Traceback (most recent call last):
#   File "<python-input-126>", line 1, in <module>
#     counter()
#     ~~~~~~~^^
#   File "<python-input-123>", line 4, in increment
#     counter += 1
#     ^^^^^^^
# UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value
def create_counter():
    counter = 0
    def increment():
        nonlocal counter
        counter += 1
        return counter
    
    return increment

counter()
# Traceback (most recent call last):
#   File "<python-input-128>", line 1, in <module>
#     counter()
#     ~~~~~~~^^
#   File "<python-input-123>", line 4, in increment
#     counter += 1
#     ^^^^^^^
# UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value
counter = create_counter()
counter()
# 1
counter()
# 2
counter()
# 3

# Bardzo sie ciesze ze wykonalem calosc w terminalu. Na poczatku, potwierdzilem sobie w glowie, ze bez nonlocal, ten przypadke sie wywali. To jest jasne.
# Jednakze, odkrylem ze jesli funkcja zostanie zdefiniowana, przypisana do zmiennej.
# Nastepnie zmieniona, to zmiana tej funkcji NIE ma od razu przelo enia na ta zmienna.
# Poniewaz siedzi w memory. Zgodnie z wczesniejszymi wytłumaczeniami działania przypisywania referencji do zmiennych i share-owania obiektów.
# wiec trzeba zdefiniowac na nowo zmienna wraz z updated function.

# Exercise 40 - Closure
def create_multiplier(factor):
    print(f"create_multiplier factor: {factor}")

    def multiply(number):
        print(f"multiply number: {number}")
        print(f"return number factor: {number * factor}")
        return number * factor
    
    return multiply

double = create_multiplier(2)
# create_multiplier factor: 2
double
# <function create_multiplier.<locals>.multiply at 0x105389850>
double(10)
# multiply number: 10
# return number factor: 20
# 20
triple = create_multiplier(3)
# create_multiplier factor: 3
triple(10)
# multiply number: 10
# return number factor: 30
# 30

# Exercise 41 - First-Class Functions
def add(a, b):
    a + b

def multiply(a, b):
    a * b

def calculate(operation, a, b):
    return operation(a, b)

calculate(add, 2, 3)
# 5
calculate(multiply, 4, 4)
# 16
