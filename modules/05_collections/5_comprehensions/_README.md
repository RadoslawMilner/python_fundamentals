## Module 05 — Comprehensions
Comprehensions pozwalają tworzyć nowe kolekcje na podstawie istniejących iterable objects.

Najważniejsza idea: zastępują typowe pętle służące do budowania kolekcji.

1. List Comprehension
Zacznijmy od klasycznej pętli:
```python
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)
```

Ten sam rezultat można uzyskać krócej:
```python
squares = [num ** 2 for num in numbers]
```

Składnia:
```python
[expression for item in iterable]
```

Kolejność jest istotna:
1. expression — co chcemy umieścić w nowej liście.
2. for item — po czym iterujemy.
3. in iterable — źródło danych.
2. Filtering

Możemy również dodawać warunki:
```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
```

Składnia:
```python
[expression for item in iterable if condition]
```

Warunek decyduje, czy element zostanie uwzględniony.

3. Transformation + Filtering
Możemy jednocześnie filtrować i przekształcać:
```python
numbers = [1, 2, 3, 4, 5, 6]
result = [num ** 2 for num in numbers if num % 2 == 0]
```

Wynik:
```python
[4, 16, 36]
```

Zauważ różnicę:
- if na końcu filtruje elementy.
- expression określa, co trafia do nowej kolekcji.

4. Conditional Expression
Możemy też użyć if/else wewnątrz expression:
```python
labels = ["even" if num % 2 == 0 else "odd" for num in numbers]
```

Ważna różnica składniowa:
| Cel |	Składnia |
| - | - |
| Filtrowanie	| for ... if condition |
| Wybór wartości | value_if_true if condition else value_if_false |
