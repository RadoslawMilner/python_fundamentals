# Module 06.2 - Strings: String Methods

# Exercise 68 - Cleaning Data
raw_data = "   ###Python Developer###   "
raw_data.strip().strip('#').lower()
# 'python developer'
# Answer: Yes and No. For use lower in this case, it does not matter. But to strip '#', there cannot be any leading extra whitespaces, becase, if they are, then these hashes are not leading.

# Exercise 69 - Validation
filenames = [
    "report.csv",
    "image.png",
    "data.json",
    "backup.csv",
    "notes.txt"
]
new_list = [filename for filename in filenames if filename.endswith('.csv')]
new_list
# ['report.csv', 'backup.csv']

# Exercise 70 - Searching
text = "Python is great. Python is powerful."
text.find('Python')
# 0
text.find('powerful')
# 27
text.find('Ruby')
# -1
text.index('Ruby')
# Traceback (most recent call last):
#   File "<python-input-206>", line 1, in <module>
#     text.index('Ruby')
#     ~~~~~~~~~~^^^^^^^^
# ValueError: substring not found

# Exercise 71 - Parsing & Joining
record = "Alex;32;Warsaw;Engineer"
' | '.join(record.split(';')).replace('Warsaw', 'Wroclaw')
# 'Alex | 32 | Wroclaw | Engineer'

# Exercise 72 - Practical Data Cleaning
emails = [
    "  Alex@Example.com ",
    "maria@gmail.com",
    " JOHN@EXAMPLE.COM  ",
    "peter@yahoo.com "
]
new_list = [email.strip().lower() for email in emails]
# ['alex@example.com', 'maria@gmail.com', 'john@example.com', 'peter@yahoo.com']

# Exercise 73 — Data Normalization Pipeline
raw_emails = [
    "  Alex@Example.com ",
    "MARIA@GMAIL.COM",
    " john@example.com ",
    "",
    "   ",
    "Peter@Yahoo.com"
]
# lets add duplicated values. I am aware of fact, that after normalization, there will be 2x [''].
raw_emails.extend(raw_emails)
raw_emails
[
    '  Alex@Example.com ',
    'MARIA@GMAIL.COM',
    ' john@example.com ',
    '',
    '   ',
    'Peter@Yahoo.com',
    '  Alex@Example.com ',
    'MARIA@GMAIL.COM',
    ' john@example.com ',
    '', 
    '   ',
    'Peter@Yahoo.com'
]

def normalize_emails(raw_emails):
    result = []
    seen = set()
    for email in raw_emails:
        normalized_email = email.strip().lower()
        if normalized_email == '' or normalized_email in seen:
            continue
        seen.add(normalized_email)
        result.append(normalized_email)

    return result

normalize_emails(raw_emails)
# ['alex@example.com', 'maria@gmail.com', 'john@example.com', 'peter@yahoo.com']

# Exercise 74 — Data Normalization Pipeline, next step
records = [
    " Alex ; 32 ; Warsaw ",
    "Maria;28;London",
    " alex ; 32 ; Warsaw ",
    "John;abc;Berlin",
    "Peter;25;Paris",
    "Maria;28;London",
    "Bob;28;Athens"
]

def data_normalization(records):
    def normalize(records):
        splitted_records = [record.split(';') for record in records]
        stripped_split_records = []
        for mini_list in splitted_records:
            new_list = []
            new_tuple = tuple(new_list)
            for record in mini_list:
                new_list.append(record.strip())
            stripped_split_records.append(new_tuple)

        return stripped_split_records

    def validation():
        normalized_records = normalize(records)
        validated_records = []
        seen = set()
        for mini_tuple in normalized_records:
            name, age, city = mini_tuple
            if not age.isdigit() or mini_tuple in seen:
                continue
            mini_dict = dict(name = name, age = int(age), city = city)
            seen.add(mini_tuple)
            validated_records.append(mini_dict)

        return validated_records
    
    return validation()

data_normalization(records)
# [{'name': 'Alex', 'age': 32, 'city': 'Warsaw'}, {'name': 'Maria', 'age': 28, 'city': 'London'}, {'name': 'alex', 'age': 32, 'city': 'Warsaw'}, {'name': 'Peter', 'age': 25, 'city': 'Paris'}, {'name': 'Bob', 'age': 28, 'city': 'Athens'}]
