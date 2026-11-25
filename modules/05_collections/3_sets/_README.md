## Module 05 — Collections: Sets

Teraz przechodzimy do struktury, która będzie szczególnie ważna w algorytmach.
1. Theory
Set to kolekcja unikalnych elementów.
```python
numbers = {1, 2, 3, 3, 4}
```

Wynik:
```python
{1, 2, 3, 4}
```

Najważniejsze właściwości:
| Property | Set |
| - | - |
| Unique elements	| Yes |
| Mutable |	Yes |
| Ordered |	No |
| Indexing |	No |
| Duplicates |	No |

Creating sets
```python
numbers = {1, 2, 3}
empty_set = set()
```

Uwaga: {} tworzy pusty dictionary, a nie set.

Adding and removing

| Operation | Purpose |
| - | - |
| add(x) | Dodaje element |
| update(iterable) | Dodaje wiele elementów |
| remove(x) | Usuwa element, KeyError jeśli brak |
| discard(x) | Usuwa element, bez błędu jeśli brak |
| pop() | Usuwa i zwraca dowolny element |
| clear() | Czyści set |

Membership testing
```python
numbers = {10, 20, 30}

20 in numbers
```

Średnia złożoność czasowa sprawdzenia przynależności wynosi O(1).

To ogromna różnica względem listy, gdzie membership testing wynosi O(n).
```
┌─────────────────────────────────────────────────────────────────────┐
│ OPERACJE NA ZBIORACH — SET OPERATIONS                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  UNION (suma)                                                       │
│  A ∪ B — elementy występujące w A lub B                             │
│                                                                     │
│  INTERSECTION (część wspólna)                                       │
│  A ∩ B — elementy występujące w obu zbiorach                        │
│                                                                     │
│  DIFFERENCE (różnica)                                               │
│  A - B — elementy A, których nie ma w B                             │
│                                                                     │
│  SYMMETRIC DIFFERENCE (różnica symetryczna)                         │
│  A △ B — elementy występujące tylko w jednym ze zbiorów             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

Elementy występujące tylko w jednym ze zbiorów.

Przykład:
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a | b
a & b
a - b
a ^ b
```


