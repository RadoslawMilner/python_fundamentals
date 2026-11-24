# Module 05.5 — Collections: Comprehensions

# [expression for item in iterable]
# Kolejność jest istotna:
# 1. expression — co chcemy umieścić w nowej liście.
# 2. for item — po czym iterujemy.
# 3. in iterable — źródło danyc

# with filtering
# [expression for item in iterable if condition]

# conditional expression
# [condition in expression for item in iterable
# Ważna różnica składniowa:
# Cel	              Składnia
# Filtrowanie	      for ... if condition
# Wybór wartości	  value_if_true if condition else value_if_false

# Exercise 58 - Transformation
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [num ** 2 for num in numbers]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_numbers = [num for num in numbers if num % 2 == 0]
# [2, 4, 6, 8, 10]
even_squares = [num ** 2 for num in numbers if num % 2 == 0]
# [4, 16, 36, 64, 100]
labels = ['even' if num % 2 == 0 else 'odd' for num in numbers]
# ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']

# Exercise 59 - Strings
words = ["python", "ruby", "javascript", "go", "java"]
uppercased = [word.upper() for word in words]
uppercased
# ['PYTHON', 'RUBY', 'JAVASCRIPT', 'GO', 'JAVA']
word_lengths = [len(word) for word in words]
word_lengths
# [6, 4, 10, 2, 4]
words_above_4_chars = [word for word in words if len(word) > 4]
words_above_4_chars
# ['python', 'javascript']
uppercased_words_above_4_chars = [word.upper() for word in words if len(word) > 4]
uppercased_words_above_4_chars
# ['PYTHON', 'JAVASCRIPT']

# Exercise 60 - Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]
new_dict = {num: num ** 2 for num in numbers}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Exercise 61 - Set Comprehension
numbers = [1, 2, 2, 3, 3, 4, 5, 5, 6]
set_with_squared = {num ** 2 for num in numbers}
set_with_squared
# {1, 4, 36, 9, 16, 25}
set_with_even = {num for num in numbers if num % 2 == 0}
set_with_even
# {2, 4, 6}
words = ["python", "ruby", "javascript", "go", "java"]
set_with_word_lengths = {len(word) for word in words}
set_with_word_lengths
# {10, 2, 4, 6}

# Exercise 62 - Nested Comprehensions
# 62.1 Flatten
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
flattened = [num for row in matrix for num in row]
flattened
[1, 2, 3, 4, 5, 6]
# 62.2 Filter nested elements
flattened_even = [num for row in matrix for num in row if num % 2 == 0]
flattened_even
# [2, 4, 6]
# 62.3 Transform nested elements
flattened_squared = [num ** 2 for row in matrix for num in row]
flattened_squared
# [1, 4, 9, 16, 25, 36]
# 62.4 Nested filtering
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened_squared_above_5 = [num ** 2 for row in matrix for num in row if num > 5]
flattened_squared_above_5
# [36, 49, 64, 81]
