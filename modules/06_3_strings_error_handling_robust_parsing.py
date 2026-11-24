# Module 06.3 - Strings: Error Handling & Robust Parsing

# Exercise 75 - Exception Basics
int('42')
# 42
int('abc')
# Traceback (most recent call last):
#   File "<python-input-452>", line 1, in <module>
#     int('abc')
#     ~~~^^^^^^^
# ValueError: invalid literal for int() with base 10: 'abc'
try:
    int('42')
except ValueError:
    print('Invalid integer')
# 42

try:
    int('abc')
except ValueError:
    print('Invalid integer')
# Invalid integer

try:
    age = int('abc')
except ValueError:
    print('Invalid integer')
else:
    print(age)
# Invalid integer

try:
    age = int('42')
except ValueError:
    print('Invalid integer')
else:
    print(age)
# 42

try:
    age = int('42')
except ValueError:
    print('Invalid integer')
else:
    print(age)
finally:
    print('Conversion finished')
# 42
# Conversion finished

try:
    age = int('abc')
except ValueError:
    print('Invalid integer')
else:
    print(age)
finally:
    print('Conversion finished')
# Invalid integer
# Conversion finished

# Exercise 76 - EAFP vs LBYL
values = ["42", "abc", "-15", "3.14", ""]

# LBYL — Look Before You Leap.
def convert_lbyl(value):
    if value.isdigit():
        return int(value)

# EAFP - Easier to Ask Forgiveness than Permission.
def convert_eafp(value):
    try:
        return int(value)
        # return float(value)
    except ValueError:
        return 'Invalid value'

[convert_lbyl(value) for value in values]
# [42, None, None, None, None]
[convert_eafp(value) for value in values]
# [42, 'Invalid value', -15, 'Invalid value', 'Invalid value'] - with int
[convert_eafp(value) for value in values]
# [42.0, 'Invalid value', -15.0, 3.14, 'Invalid value'] - with float

# Exercise 77 - Robust Data Normalization
records = [
    " Alex ; 32 ; Warsaw ",
    "Maria;28;London",
    "John;abc;Berlin",
    "Peter;-25;Paris",
    "Kate;3.14;Madrid",
    "Bob;28;Athens",
    "Dan;Barcelona",
    "Alice",
    "Dan;38;Chicago;Doctor",
]

# WAZNE IMPORTANT !!!
def converted_records(records):
    # parsing data:
    split_records = [record.split(';') for record in records]
    stripped_split_records = []
    for record in split_records:
        new_list = []
        for field in record:
            new_list.append(field.strip())
        stripped_split_records.append(tuple(new_list))

    records_with_3_fields = [record for record in stripped_split_records if len(record) == 3]

    # transformation data:    
    def convert_age(value):
        try:
            return int(value)
        except ValueError:
            return None

    # validation data:
    converted_records = []
    for record in records_with_3_fields:
        name, age, city = record
        converted_age = convert_age(age)
        if converted_age is None:
            continue
        new_dict = dict(name = name, age = converted_age, city = city)
        converted_records.append(new_dict)

    return converted_records

converted_records(records)
# [{'name': 'Alex', 'age': 32, 'city': 'Warsaw'}, {'name': 'Maria', 'age': 28, 'city': 'London'}, {'name': 'Peter', 'age': -25, 'city': 'Paris'}, {'name': 'Bob', 'age': 28, 'city': 'Athens'}]
