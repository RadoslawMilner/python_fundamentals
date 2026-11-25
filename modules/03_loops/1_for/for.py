# Module 03.1 — Loops: for

# Exercise 1 - Sum of Numbers
numbers = [4, 8, 12, 16, 20]
current_sum = 0
for num in numbers:
    current_sum += num

print(current_sum)

# Exercise 2 - Count Even Numbers
numbers = [3, 8, 11, 14, 17, 20, 25, 30]
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1

print(f"The number of even numbers is: {even_count}")

# Exercise 3 - Find the Largest Number
numbers = [14, 3, 87, 42, 19, 65]
largest_number = numbers[0]
for num in numbers:
    if num > largest_number:
        largest_number = num

print(f"The largest number is: {largest_number}")

# Exercise 4 - Search with break
numbers = [5, 12, 18, 23, 31, 42]
target = 23
found = False
for num in numbers:
    if num == target:
        found = True
        break

if found:
    print(f"Number {target} found in the list.")
else:
    print(f"Number {target} not found in the list.")

# Exercise 5 - Filter with continue
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 != 0:
        continue
    print(num)

# Exercise 6 — Character Counter
text = "programming"
m_count = 0
for char in text:
    if char == "m":
        m_count += 1

print("m_count:", m_count)

# Exercise 7 - Build a New List
numbers = [2, 5, 8, 11, 14, 17, 20]
new_list = []
for num in numbers:
    if num > 10:
        new_list.append(num)

print("new_list:", new_list)

# Exercise 8 - Iterate Over a Dictionary
prices = {
    "apple": 3.50,
    "banana": 2.80,
    "orange": 4.20
}
prices_sum = 0
for fruit, price in prices.items():
    print(f"The price of {fruit} is {price}.")
    prices_sum += price

print(f"The sum of all prices is {prices_sum}.")

# Exercise 9 - Nested Loops
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum_of_elements = 0
for row in matrix:
    for element in row:
        print("Element:", element)
        sum_of_elements += element

print("Sum of all elements:", sum_of_elements)
