# Module 04.2 - Functions — Parameters, Arguments & Scope

# Exercise 21 - Keyword Arguments
def calculate_order(price, quantity, shipping_cost):
    return price * quantity + shipping_cost

print(calculate_order(shipping_cost=10, price=100, quantity=2))  # Output: 210

# Exercise 22 - Default Parameters
def calculate_order(price, quantity, shipping_cost=15):
    return price * quantity + shipping_cost

print(calculate_order(10, 2))      # Output: 35
print(calculate_order(10, 2, 20))  # Output: 40

# Exercise 23 - Local Scope (Code Analysis)
x = 100
def calculate():
    x = 50
    return x

result = calculate()
print(result) # Output: 50
print(x) # Output: 100
# x jest w bloku tej funkcji. x w funkcji jest local scope. utworzonym w tej funkcji. dostepnym dla tej funkcji. nie poza nia.

# Excercise 24 - Mutable Objects (Code Analysis)
numbers = [1, 2, 3]
def add_number(collection, number):
    collection.append(number)

add_number(numbers, 4)
print(numbers) # Output: [1, 2, 3, 4]
# itemy w liście są segregowalne, zmienialne, mogą mieć zduplikwoane wartości
# zatem lista moze zostac poddana zmianie. ponadto, z dokumentacji czytam ze lista jest sekwencja. ponadto z dokumentacji rozumiem, ze jest mutable.
# nie, funkcja nie uzyla return. ta funkcja mutuje obiekt. nic nie zwraca.

# Exercise 25 - Reassignment
numbers = [1, 2, 3]
def modify(collection):
    collection = [10, 20, 30]

modify(numbers)
print(numbers) # Output: [1, 2, 3]
# Because numbers is the global scope variable. The collection is the local scope in the function. It does not change the numbers object.

# Exercise 26 - Mutation
numbers = [1, 2, 3]
def modify(collection):
    collection.append(4)
    collection.append(5)

modify(numbers)
print(numbers) # Output: [1, 2, 3, 4, 5]
# mutation is in place change. it modifies shared object. both the caller: modify(numbers) and the function itself point to the same identity. then, these changes persists outside function.
# reassignment is a local binding. for example: collection = [ detach the local param from the original object. the callers variable remains without any change. because this rebinding is local to the function's space.

# Exercise 27 - Return vs Mutation
numbers = [1, 2, 3]
def add_number_mutate(numbers, number):
    numbers.append(number)

def add_number_copy(numbers, number):
    numbers = [10, 20, 30]
    numbers.append(number)
    return numbers

add_number_mutate(numbers, 4)
# >>> numbers
[1, 2, 3, 4]
# >>> add_number_copy(numbers, 20)
[10, 20, 30, 20]

# mam jednak pytanie dotyczace takiej budowy
def add_number_copy(numbers, number):
    numbers_copy = numbers
    numbers_copy.append(number)
    return numbers_copy

add_number_copy(numbers, 10)
# [1, 2, 3, 4, 10]
numbers
# [1, 2, 3, 4, 10]
# dlaczego? tworze nowa zmienna.
# # owszem z wykorzystaniem istniejacej lecz pod inna nazwa. jako local scope. sprawdziłem docsy.
# spisałem powyzsze wyjaśnienia. ułozyłem sobie wszystko w głowie. i nie mogę zrozumiec, dlaczego w tym przypadku add_number_copy mutuje zewn. liste.
