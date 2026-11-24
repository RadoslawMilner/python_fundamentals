# Module 01 — Variables, Data Types & Operators

# Exercise 1 – Temperature Converter
celsius = 25
fahrenheit = celsius * (9/5) + 32
print(fahrenheit)

# Exercise 2 – Number Classification
number = 17
is_number_even = number % 2 == 0
print(f"Is the number even? {is_number_even}")
is_number_larger_than_ten = number > 10
print(f"Is the number larger than ten? {is_number_larger_than_ten}")
is_number_positive = number > 0
print(f"Is the number positive? {is_number_positive}")

# Exercise 3 – Shopping Cart
item_price = 89.99
quantity = 3
discount = 0.10
shipping_cost = 15.00

items_value = item_price * quantity
print(f"items_value: {items_value}.")
calculated_discount = 1 - discount
print(f"calculated_discount: {calculated_discount}.")
singular_item_price_after_discount = item_price * calculated_discount
print(f"singular_item_price_after_discount: {singular_item_price_after_discount}.")
discounted_items_value = singular_item_price_after_discount * quantity
print(f"discounted_items_value: {discounted_items_value}.")
order_price = discounted_items_value + shipping_cost
print(f"order_price: {order_price}.")
