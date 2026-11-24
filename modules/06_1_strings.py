# Module 06.1 - Strings

# Exercise 63 - Indexing & Slicing
text = "DataEngineering"
# 63.1
text[0]
'D'
# 63.2
text[-1]
# 'g'
# 63.3
text[:4]
# 'Data'
# 63.4
text[-4:]
# 'ring'
# 63.5
# text[4:10]
'Engine'
# 63.6
text[::-1]
# 'gnireenignEataD'
# 63.7
text[::2]
# 'DtEgneig'

# Exercise 64 - Immutability
# 64.1
text = "python"
text[0].upper()
# 'P'
text
'python'
text[0] = 'P'
# Traceback (most recent call last):
#   File "<python-input-35>", line 1, in <module>
#     text[0] = 'P'
#     ~~~~^^^
# TypeError: 'str' object does not support item assignment
text.capitalize()
# 'Python'
text
# 'python'
# 64.2
# Answer: I really didn't know. Till I done 3rd subtask. Both slicing and upper RETURN string. Not modify it.
# # Therefore we can return output and asign it to new variable. Because, as proven before, the string is immutable.
# 64.3
new_string = text[:1].upper() + text[1:]
new_string
# 'Python'

# Exercicse 65 - Iteration
text = 'programming'
# 65.1
chars_number = 0
for char in text:
    chars_number += 1

chars_number
# 11
# 65.2
g_occurences = 0
for char in text:
    if char == 'g':
        g_occurences += 1

g_occurences
# 2
# 65.3
vowels = ('a', 'e', 'i', 'o', 'u')
new_string = ''
for char in text:
    if char in vowels:
        new_string += char

new_string
# 'oai'
# 65.4
# first lets add some spaces to our text
text_with_spaces = ''
for char in text:
    text_with_spaces += char
    text_with_spaces += ' '

text_with_spaces
# 'p r o g r a m m i n g '
# second lets rempve these spaces
new_string2 = ''
for char in text_with_spaces:
    if char != ' ':
        new_string2 += char

new_string2
# 'programming'

# Exercise 66 - Membership & String Methods
text = "Data Engineering with Python"
# 66.1
"Python" in text
# True
# 66.2
"Ruby" in text
# False
# 66.3
vowels = ('a', 'e', 'i', 'o', 'u')
result = ''.join([char for char in text if char in vowels])
# join przyjmuje dowolny iterable stringów, więc nie musisz najpierw tworzyć listy. then even:
# result = ''.join(char for char in text if char in vowels)
result
# 'aaieeiio'
# 66.4
text.replace(' ', '')
# 'DataEngineeringwithPython'
# 66.5
text.lower()
# 'data engineering with python'
# 66.6
text.count('a')
# 2
# 66 Bonus question -> Answer: because string in pyhton is case sensitive. 
'p' == 'P'
# False
# strings 'p' and 'P' are different values

# Exercise 67 - String Parsing
# nearly case from real life. great!
record = "name=Alex;age=32;city=Warsaw;role=Engineer"
# first approach:
pairs = [pair.split('=') for pair in record.split(';')]
new_dict = {pair[0]: pair[1] for pair in pairs}
new_dict
# {'name': 'Alex', 'age': '32', 'city': 'Warsaw', 'role': 'Engineer'}
# second approach:
new_dict = {}
for pair in record.split(';'):
    key, value = pair.split('=')
    new_dict[key] = value

new_dict
# {'name': 'Alex', 'age': '32', 'city': 'Warsaw', 'role': 'Engineer'}
