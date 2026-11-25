## Module 05 — Collections
Teraz zaczyna się bardzo ważna część. Poznamy cztery podstawowe struktury danych Pythona:

  1. List — list

    Ordered, mutable, allows duplicates.

    Przykład: [10, 20, 20, 30]

  2. Tuple — tuple

    Ordered, immutable, allows duplicates.

    Przykład: (10, 20, 20, 30)

  3. Set — set

    Mutable, unique elements, no positional indexing.

    Przykład: {10, 20, 30}

  4. Dictionary — dict

    Mutable, key-value mapping, unique keys, insertion ordered.

    Przykład: {"name": "Alex", "age": 30}

## Module 05 — Collections: Lists
1. List — teoria
Listy już znasz, ale teraz spojrzymy na nie bardziej systematycznie.
Creating and accessing
```python
numbers = [10, 20, 30, 40, 50]
numbers[0]    # 10
numbers[-1]   # 50
numbers[1:4]  # [20, 30, 40]
```

Ważne:
- Indeksy zaczynają się od 0.
- Indeksy ujemne liczą od końca.
- Slicing nie uwzględnia górnej granicy.

Modifying
Najważniejsze operacje:
| Operation |	Purpose |
| - | - |
| append(x) |	Dodaje jeden element na końcu |
| extend(iterable) |	Dodaje elementy z iterowalnego obiektu |
| insert(i, x) | Wstawia element pod indeksem |
| remove(x) |	Usuwa pierwsze wystąpienie wartości |
| pop(i) | Usuwa i zwraca element |
| clear() | Usuwa wszystkie elementy |
| copy() | Tworzy shallow copy |

Szczególnie zwróć uwagę na różnicę:
```python
numbers.append([60, 70])
```
vs
```python
numbers.extend([60, 70])
```

Pierwsza operacja dodaje jeden element będący listą. Druga dodaje dwa osobne elementy.

Mini-lesson — List Methods
Jeszcze jedna ważna rzecz przed kolejnym zestawem.

Metody takie jak:
- append()
- extend()
- insert()
- remove()
- sort()
- reverse()
modyfikują istniejącą listę i zazwyczaj zwracają None.

Natomiast:
- sorted()
- reversed()
zwracają nowe iteratory lub kolekcje zależnie od operacji.

To ważne rozróżnienie, szczególnie gdy zaczniesz łączyć metody.