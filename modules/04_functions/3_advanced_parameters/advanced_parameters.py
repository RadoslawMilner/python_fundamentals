# Module 04.3 - Functions: Advanced Parameters

# Exercise 28 - Variable Arguments (*args)
def calculate_average(*args):
    if args:
        result = 0
        count = 0
        for num in args:
            result += num
            count += 1
        return result / count
    else:
        return None

calculate_average(10, 20, 30)
# 20.0
calculate_average(5, 15)
# 10.0
calculate_average()
# >>>
# Podejście	Zachowanie - return None	Brak wyniku. Poniewaz dane moga byc puste dla sredniej. Moga tez byc ujemne. Natomiast nie jest to taki sam cel jak dla znalezienia najwiekszej, gdzie wtedy konieczne sa dane.

# Exercise 29 - Keyword Arguments (**kwargs)
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

describe_person(name="Alex", age=30, city="Warsaw")
# name Alex
# age 30
# city Warsaw

# Exercise 30 - Combing Parameters
def create_product(name, price, quantity=1, **kwargs):
    return dict(
        name = name,
        price = price,
        quantity = quantity,
        order_value = price * quantity,
        extra_info = kwargs
    )

create_product("Laptop", 4500, 2, category="Electronics", brand="Lenovo")
# {'name': 'Laptop', 'price': 4500, 'quantity': 2, 'order_value': 9000, 'extra_info': {'category': 'Electronics', 'brand': 'Lenovo'}}

# Exercise 31 - Keyword-only Arguments
def calculate_shipping(weight, *, express=False, insurance=False):
    # weight does not influence anything in assuptions
    base_cost = 15
    total = base_cost
    if express:
        total += 20
    if insurance:
        total += 10
    return total

calculate_shipping(10, express=False, insurance=False)
# 15
calculate_shipping(10, express=True, insurance=False)
# 35
calculate_shipping(10, express=False, insurance=True)
# 25
calculate_shipping(10, express=True, insurance=True)
# 45

# Exercise 32 - Mutable Default Argument
def add_item(item, items=[]):
    items.append(item)
    return items

first = add_item("apple")
second = add_item("banana")

print(first) # Output: ['apple', 'banana']
print(second) # Output: ['apple', 'banana']

# First and second have same elements, because, when to first has been assigned add_item("apple") call function, then this first was ["apple"]
# With second call, the items has been mutated. it is still one object, which has been assigned to two variables. which are now share 1 object.
# it is incorrect to define function with mutable default param. This default param should be items=None. And should be added a condition at the start of the function, to check if items is None
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

# now we create a new list/object. with each call that function we just add item, to new list. ofcourse, due to fact, that this is still default param, we can pass some list also.
first = add_item("apple")
first
# ['apple']
second = add_item("banana")
first
# ['apple']
second
# ['banana']
add_item("mango", ["tree", "dog", "hill"])
# ['tree', 'dog', 'hill', 'mango']
