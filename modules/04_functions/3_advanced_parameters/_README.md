## Module 04 — Functions: Advanced Parameters

Teraz rozszerzamy sposób przekazywania argumentów do funkcji. To ważny element Pythona, szczególnie przy projektowaniu API, bibliotek i komponentów wielokrotnego użytku.

1. Positional Arguments
Argumenty przekazywane według kolejności parametrów.
```python
def calculate(price, quantity):
    return price * quantity
    
calculate(100, 3)
```

100 trafia do price, a 3 do quantity.

2. Keyword Arguments
Argumenty przekazywane przez nazwę parametru.
```python
calculate(quantity=3, price=100)
```

Kolejność nie ma znaczenia.

Możesz też mieszać oba sposoby, ale argumenty pozycyjne muszą wystąpić przed nazwanymi:
```python
calculate(100, quantity=3)
```

3. Default Parameters
Wartości domyślne:
```python
def calculate(price, quantity=1):
    return price * quantity
```

Możesz wywołać calculate(100) albo calculate(100, 5).

Ważna pułapka: unikaj mutowalnych wartości domyślnych.

Nie rób tego:
```python
def add_item(item, items=[]):
    items.append(item)    
    return items
```

Dlaczego? Python tworzy tę listę tylko raz — podczas definiowania funkcji. Kolejne wywołania mogą współdzielić tę samą listę.

Bezpieczny idiom:
```python
def add_item(item, items=None):
    if items is None:
          items = []
    items.append(item)
    return items
```

Do tego problemu jeszcze wrócimy.

4. *args — Variable Positional Arguments
Pozwala przyjąć dowolną liczbę argumentów pozycyjnych.
```python
def calculate_sum(*args):
    total = 0
    for number in args:
        total += number
    return total

calculate_sum(10, 20, 30)
```

args jest tuple.

Nazwa args jest konwencją. Gwiazdka * ma znaczenie składniowe.
5. **kwargs — Variable Keyword Arguments
Pozwala przyjąć dowolną liczbę argumentów nazwanych.
```python
def create_user(**kwargs):
    return kwargs
      
create_user(name="Alex", age=30, active=True)
```

kwargs jest dictionary.

Ponownie: nazwa jest konwencją, a ** jest elementem składni.
6. Keyword-only Arguments
Możesz wymusić przekazywanie wybranych parametrów przez nazwę.
```python
def create_user(name, *, active=True):
    return name, active
```

Poprawnie:
```python
create_user("Alex", active=False)
```

Niepoprawnie:
```python
create_user("Alex", False)
```

Separator * oznacza, że parametry występujące po nim muszą być keyword-only.