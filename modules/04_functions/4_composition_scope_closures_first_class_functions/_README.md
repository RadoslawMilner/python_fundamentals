Ważny temat: Python Function Argument Model
Zatrzymajmy się na chwilę przy jednej koncepcji, która łączy kilka poprzednich lekcji.

Python stosuje model przekazywania argumentów określany jako call by sharing (czasami nazywany pass by object reference).

W praktyce:
- funkcja otrzymuje lokalną nazwę powiązaną z przekazanym obiektem;
- mutacja obiektu jest widoczna poza funkcją;
- przypisanie nowego obiektu do lokalnej nazwy nie zmienia powiązania nazwy u wywołującego.
To wyjaśnia jednocześnie:
- Exercise 24 — mutation;
- Exercise 25 — reassignment;
- Exercise 27 — copy vs mutation;
- Exercise 32 — mutable default argument.
To nie są cztery niezależne problemy. To konsekwencje jednego modelu działania języka

## Następny krok — Functions: Composition & Scope
Teraz przejdziemy do bardziej praktycznego projektowania funkcji.

Poznamy:
1. Funkcje wywołujące inne funkcje.
2. return i early return.
3. Local, global i nonlocal scope.
4. Funkcje jako obiekty (first-class functions).
5. Docstrings i type hints.

## Module 04 — Functions: Scope, Closures & First-Class Functions
To ostatnia część modułu Functions. Poznamy mechanizmy, które później spotkasz w bibliotekach, frameworkach, dekoratorach i architekturze aplikacji.

1. Nested Functions
Python pozwala definiować funkcje wewnątrz innych funkcji.
```python
def outer():
    def inner():
        print("Inside inner")

    inner()

outer()
```

inner() jest dostępna lokalnie wewnątrz outer().

Przydaje się to, gdy jakaś operacja ma sens wyłącznie jako część większej operacji.

2. Scope — LEGB Rule
Python szuka nazw według następującej kolejności:

| Scope | Znaczenie |
| - | - |
| L — Local |	Bieżąca funkcja |
| E — Enclosing |	Funkcja zewnętrzna |
| G — Global |	Poziom modułu |
| B — Built-in |	Wbudowane nazwy Pythona |

Przykład:
```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)
    
    inner()
    
outer()
```

Wynik: local.

Python znajduje pierwsze pasujące powiązanie nazwy, idąc od Local do Built-in.

3. nonlocal
Pozwala funkcji wewnętrznej zmodyfikować zmienną z zakresu funkcji zewnętrznej.
```python
def outer():
    counter = 0
    
    def inner():
        nonlocal counter
        counter += 1
    
    inner()
    return counter
```

Wynik outer() to 1.

Bez nonlocal przypisanie counter += 1 traktowałoby counter jako lokalną nazwę funkcji inner().

4. Closures
Closure powstaje, gdy funkcja wewnętrzna zachowuje dostęp do zmiennych z funkcji zewnętrznej, nawet po zakończeniu wykonania funkcji zewnętrznej.
```python
def create_multiplier(factor):
    def multiply(number):
        return number * factor
    
    return multiply
    
double = create_multiplier(2)
triple = create_multiplier(3)
```

Teraz:
- double(5) → 10
- triple(5) → 15

Dlaczego?

multiply zachowuje dostęp do factor z otaczającego scope.

Nie potrzebujemy globalnych zmiennych ani klas, żeby przechowywać taki stan.

5. First-Class Functions
W Pythonie funkcje są obiektami pierwszej klasy (first-class objects).

Oznacza to, że możesz:
- przypisać funkcję do zmiennej;
- przekazać funkcję jako argument;
- zwrócić funkcję z innej funkcji;
- przechowywać funkcje w kolekcjach.
Przykład:
```python
def greet():
    return "Hello"
    
say_hello = greet
```

Teraz say_hello() wywołuje tę samą funkcję.

Ważne rozróżnienie:
- greet — referencja do funkcji.
- greet() — wykonanie funkcji.
To podstawa callbacków, dekoratorów i wielu mechanizmów frameworków.