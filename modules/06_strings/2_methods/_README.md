## Module 06 — Strings: String Methods

Dotychczas poznaliśmy podstawowe operacje na stringach. Teraz rozszerzymy je o metody wykorzystywane przy czyszczeniu, walidacji i parsowaniu danych.

1. Whitespace — strip(), lstrip(), rstrip()
Whitespace to m.in. spacje, tabulatory i znaki nowej linii.
```python
text = "   Python Developer   "
text.strip()   # "Python Developer"
text.lstrip()  # "Python Developer   "
text.rstrip()  # "   Python Developer"
```

Możesz też przekazać zbiór znaków do usunięcia:
```python
text = "###Python###"
text.strip("#")  # "Python"
```

Uwaga: strip("#") usuwa wskazane znaki z obu końców, a nie konkretny podciąg znaków.

2. Prefix & Suffix — startswith(), endswith()
Przydatne przy walidacji i klasyfikacji tekstu.
```python
filename = "report.csv"
filename.startswith("report")  # True
filename.endswith(".csv")     # True
```

Obie metody zwracają boolean.

3. Searching — find() i index()
Obie metody szukają podciągu.
```python
text = "Python Programming"
text.find("Pro")   # 7
text.index("Pro")  # 7
```

Różnica:
| Metoda | Gdy nie znajdzie tekstu |
| - | - |
| find() | Zwraca -1 |
| index() | Rzuca ValueError |

Do bezpiecznego wyszukiwania często wygodniejszy jest find().

4. Replacing — replace()
```python
text = "I like Ruby"
text.replace("Ruby", "Python")
# "I like Python"
```

Możesz ograniczyć liczbę zamian:
```python
text = "apple apple apple"
text.replace("apple", "orange", 1)
# "orange apple apple"
```

5. Splitting & Joining
Poznaliśmy już oba mechanizmy, ale teraz uporządkujmy ich relację.

split() dzieli string na listę:
```python
record = "Alex;32;Warsaw"
record.split(";")
# ["Alex", "32", "Warsaw"]
```

join() łączy iterable stringów w jeden string:
```python
parts = ["Alex", "32", "Warsaw"]
" | ".join(parts)
# "Alex | 32 | Warsaw"
```

Ważne: join() jest metodą separatora, a nie listy.