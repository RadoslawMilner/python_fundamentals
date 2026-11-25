## Module 05 — Dictionaries
Dictionary (dict) przechowuje dane w postaci par key → value.
```python
user = {
    "name": "Alex",
    "age": 30,
    "active": True
}
```

Właściwości:
- Mutable — można zmieniać zawartość.
- Keys są unikalne.
- Keys muszą być hashable (np. str, int, tuple zawierający hashable values).
- Values mogą być dowolnymi obiektami.
- Zachowuje kolejność wstawiania elementów (Python 3.7+).

1. Odczyt i modyfikacja
```python
user["name"]              # "Alex"
user["age"] = 31          # aktualizacja
user["city"] = "Warsaw"   # dodanie
```

Uwaga: odczyt nieistniejącego klucza przez user["email"] powoduje KeyError.

Bezpieczniejsza alternatywa:
```python
user.get("email")           # None
user.get("email", "N/A")    # "N/A"
```

2. Usuwanie
| Operacja | Działanie |
| pop(key) | Usuwa klucz i zwraca jego wartość |
| popitem() |	Usuwa i zwraca ostatnią parę |
| del dict[key] | Usuwa wskazany klucz |
| clear() |	Usuwa wszystkie elementy |

3. Iterowanie
```python
for key in user:
    print(key)

for value in user.values():
    print(value)

for key, value in user.items():
    print(key, value)
```

Zapamiętaj: .items() zwraca pary (key, value).

4. Membership
```python
"name" in user
```

Sprawdza obecność klucza, nie wartości.

Średnia złożoność wyszukiwania klucza: O(1).