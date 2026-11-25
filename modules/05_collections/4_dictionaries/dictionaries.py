# Module 05.4 — Collections: Dictionaries

# Exercise 54 - Dictionary Basics
person = dict(name = 'Alex', age = 30, city = 'London')
person
# {'name': 'Alex', 'age': 30, 'city': 'London'}
person['name']
# 'Alex'
person['age'] = 31
person
# {'name': 'Alex', 'age': 31, 'city': 'London'}
person['profession'] = 'Engineer'
person
# {'name': 'Alex', 'age': 31, 'city': 'London', 'profession': 'Engineer'}
del person['city']
person
'profession' in person
True
# {'name': 'Alex', 'age': 31, 'profession': 'Engineer'}
person.get('email')
# >>>

# Exercise 55 - Iteration
def products_data(products):
    products_names = []
    for name in products:
        products_names.append(name)

    prices = []
    total_value = 0
    for price in products.values():
        prices.append(price)
        total_value += price

    most_pricey = 0
    most_pricey_product = ()
    for product, price in products.items():
        if price > most_pricey:
            most_pricey = price
            most_pricey_product = (product, price)

    return dict(products_names = products_names, prices = prices, total_value = total_value, most_pricey = most_pricey_product)

# Exercise 56 - Frequency Counter
words = ["apple", "banana", "apple", "orange",
         "banana", "apple", "pear", "orange"]
new_dict = dict()
for word in words:
    if word in new_dict:
        new_dict[word] += 1
    else:
        new_dict[word] = 1

new_dict
# {'apple': 3, 'banana': 2, 'orange': 2, 'pear': 1}

# Exercise 57 - Dictionary Challenge
transactions = [
    {"user": "Alex", "amount": 100},
    {"user": "Maria", "amount": 250},
    {"user": "Alex", "amount": 50},
    {"user": "John", "amount": 300},
    {"user": "Maria", "amount": 100},
    {"user": "Alex", "amount": 200}
]
def analyze_transactions(transactions):
    new_dict = {}
    for t in transactions:
        user_name = t['user']
        total_amount = t['amount']
        # 2 ways:
        # first:
        if user_name in new_dict:
            new_dict[user_name] += total_amount
        else:
            new_dict[user_name] = total_amount
        
        # second:
        # new_dict[user_name] = new_dict.get(user_name, 0) + total_amount

    return new_dict

analyze_transactions(transactions)
# {'Alex': 350, 'Maria': 350, 'John': 300}
