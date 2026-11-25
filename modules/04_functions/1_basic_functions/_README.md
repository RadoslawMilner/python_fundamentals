## Module 04 — Functions

To jeden z najważniejszych modułów. Zaczniemy budować kod w postaci niezależnych jednostek odpowiedzialności.

Cele:
- definiowanie funkcji,
- parametry i argumenty,
- return vs print,
- lokalny i globalny scope,
- mutability i przekazywanie obiektów,
- funkcje zwracające kolekcje,
- rozbijanie problemów na mniejsze funkcje.

1. Theory — Function Basics
Defining a function
```python
def greet():
    print("Hello!")
```

def definiuje funkcję. Samo zdefiniowanie nie powoduje jej wykonania.

Wywołanie:
```python
greet()
```

Parameters vs arguments
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alex")
```

- name — parameter (parametr funkcji).
- "Alex" — argument przekazany podczas wywołania.

Multiple parameters
```python
def calculate_total(price, quantity):
    total = price * quantity
    print(total)

calculate_total(25, 4)
```

Funkcja może przyjmować wiele argumentów.
return vs print
To bardzo ważne rozróżnienie.

print() wyświetla wartość.

return przekazuje wynik z funkcji do miejsca, w którym została wywołana.
```python
def calculate_total(price, quantity):
    return price * quantity

result = calculate_total(25, 4)
print(result)
```

Dlaczego to ważne?

Wynik zwrócony przez return możesz:
- zapisać w zmiennej,
- przekazać do innej funkcji,
- wykorzystać w obliczeniach,
- zwrócić z kolejnej funkcji.
Funkcje powinny przede wszystkim dostarczać wynik, a nie zajmować się jego wyświetlaniem. Rozdzielamy logikę od prezentacji.