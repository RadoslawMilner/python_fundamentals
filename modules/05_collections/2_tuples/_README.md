## Module 05 — Collections: Tuples
1. Theory
Tuple jest uporządkowaną, niemutowalną sekwencją.
coordinates = (52.23, 21.01)

Najważniejsze właściwości:
| Property | Tuple |
| - | - |
| Ordered | Yes |
| Mutable |	No |
| Duplicates | Allowed |
| Indexing | Yes |
| Slicing |	Yes |

Accessing elements
```python
coordinates[0]   # 52.23
coordinates[-1]  # 21.01
```

Immutability
Nie możesz przypisać nowej wartości do istniejącego elementu:
```python
coordinates[0] = 50.0
```

To spowoduje TypeError.
Tuple unpacking
```python
person = ("Alex", 30, "Warsaw")

name, age, city = person
```

Python automatycznie przypisuje wartości do zmiennych.

To mechanizm, który już widziałeś przy dict.items().
Single-element tuple
Ważny szczegół składniowy:
```python
single = (10,)
```

Przecinek tworzy tuple. Same nawiasy nie wystarczą.