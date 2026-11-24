# Module 04.1 — Functions

# Exercise 17 - Basic Function
def calculate_square(number):
    return number ** 2

print(calculate_square(5))  # Output: 25

# Exercise 18 - Multiple Parameters
def calculate_discounted_price(price, discount):
    return price * (1 - discount)

print(calculate_discounted_price(200, 0.15))  # Output: 170.0

# Exercise 19 - Function with a Condition
def is_even(number):
    return number % 2 == 0

print(is_even(8))   # Output: True
print(is_even(13))  # Output: False
print(is_even(0))   # Output: True

# Exercise 20 - Reuse Previous Logic
def find_largest(numbers):
    largest_number = numbers[0]
    for num in numbers:
        if num > largest_number: largest_number = num
    return largest_number

# dodatkowo: jesli lista jest pusta, na wstepie funkcji myslalem o dodaniu warunku: if numbers:, ktory otworzy dostep do reszty funkcji.
