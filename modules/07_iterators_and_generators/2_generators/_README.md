## Module 07 — Następny krok: Generators
Teraz przechodzimy do bardzo istotnej koncepcji.

Do tej pory:
- List przechowuje całą kolekcję.
- Iterator dostarcza elementy kolejno.
- next() przesuwa jego stan.
Generator pozwala tworzyć iterator, którego elementy są produkowane na żądanie.

Przykład:
```python
def generate_numbers():
    yield 10
    yield 20
    yield 30
```

Wywołanie:
```python
numbers = generate_numbers()
```

Nie wykonuje od razu całej funkcji. Zwraca generator.

Dopiero:
```python
next(numbers)  # 10
next(numbers)  # 20
next(numbers)  # 30
```

powoduje kolejne wykonywanie funkcji.

Kluczowe nowe słowo: yield.

To będzie temat następnej lekcji. Najpierw zrozumiemy różnicę między return a yield, następnie generator functions, generator state i lazy evaluation.

# pozwolilem sobie potestowac troche i pobawic sie tym
```python
def generate_numbers():
    yield 10
    yield 20
    yield 30

numbers = generate_numbers()
type(numbers)
# <class 'generator'>

def some_function():
    return 'a'

some_variable = some_function()
some_variable
# 'a'
type(some_variable)
# <class 'str'>

def some_function():
    return 23

some_variable = some_function()
type(some_variable)
# <class 'int'>

def generator():
    yield ''

some_generator = generator()
type(some_generator)
# <class 'generator'>

next(numbers)
# 10
next(numbers)
# 20
next(numbers)
# 30
next(numbers)
# Traceback (most recent call last):
#   File "<python-input-94>", line 1, in <module>
#     next(numbers)
#     ~~~~^^^^^^^^^
# StopIteration
# >>> next(numbers)
# Traceback (most recent call last):
#   File "<python-input-95>", line 1, in <module>
#     next(numbers)
#     ~~~~^^^^^^^^^
# StopIteration
```

1. type() — Python pozwala sprawdzić rzeczywisty typ obiektu
Dokładnie tak:

```python
def some_function():
    return 23

result = some_function()

type(result)  # <class 'int'>
```

Python nie wymaga deklarowania typu zwracanego przez funkcję. Obiekt istnieje, a type() pozwala sprawdzić jego rzeczywistą klasę.

W Pythonie dodatkowo masz:

- type(obj) — dokładny typ obiektu.
- isinstance(obj, int) — sprawdzenie, czy obiekt jest instancją klasy lub jej podklasy.
- dir(obj) — dostępne atrybuty i metody.
- help(obj) — dokumentacja obiektu.

To bardzo przydatny zestaw narzędzi podczas eksplorowania nieznanego kodu.

2. return vs yield
Tu zaczyna się właściwa różnica.

| return | yield |
| - | - |
| Zwraca wartość | Produkuje wartość |
| Kończy wykonanie funkcji | Zawiesza wykonanie funkcji |
| Kolejne wywołanie zaczyna funkcję od początku | next() wznawia ją od miejsca zawieszenia |
| Zwykła funkcja | Funkcja generatorowa |

Twoje przykłady pokazują to bardzo dobrze:

```python
def some_function():
    return 23

def generator():
    yield 23
```
Pierwsza funkcja zwraca int.

Druga zwraca obiekt generator. Dopiero wywołanie next() uruchamia jej wykonanie.

3. Co dokładnie wydarzyło się przy StopIteration?
Prześledźmy Twój przykład:
```python
def generate_numbers():
    yield 10
    yield 20
    yield 30
```
Stan generatora podczas kolejnych wywołań

Pierwsze next(numbers)

10

Generator wykonuje się do pierwszego yield i zawiesza.

Drugie next(numbers)

20

Wznawia wykonanie od miejsca poprzedniego yield.

Trzecie next(numbers)

30

Dochodzi do ostatniego yield.

Czwarte next(numbers)

StopIteration
Funkcja zakończyła wykonanie. Nie ma już kolejnej wartości.

Kolejne wywołania next() również zgłoszą StopIteration. Generator jest wyczerpany.

To nie jest błąd generatora. StopIteration jest normalnym mechanizmem informującym Pythona, że iterator nie ma już elementów. Pętla for obsługuje to automatycznie

## Generator Expressions
Poznałeś już generator functions, czyli funkcje wykorzystujące yield. Python oferuje również krótszy sposób tworzenia generatorów: generator expressions.

Znasz już list comprehensions:
```python
numbers = [num * 2 for num in range(1, 6)]
```

Wynik to lista:
```python
[2, 4, 6, 8, 10]
```

Teraz zmieniamy nawiasy:
```python
numbers = (num * 2 for num in range(1, 6))
```

Wynik to generator:
```python
<class 'generator'>
```

1. Najważniejsza różnica
| List comprehension | Generator expression |
| - | - |
| [...]	| (...) |
| Tworzy całą listę | Produkuje wartości na żądanie |
| Przechowuje wszystkie wyniki | Nie materializuje całego wyniku |
| Można iterować wielokrotnie |	Po wyczerpaniu trzeba utworzyć nowy generator |

2. Generator expression w praktyce
```python
squares = (num ** 2 for num in range(1, 6))
next(squares)  # 1
next(squares)  # 4
next(squares)  # 9
```

Możesz też wykorzystać go bezpośrednio w pętli for.

3. Dlaczego generator expression używa ()?

Powód jest dość istotny:
- List comprehension tworzy kolekcję.
- Set comprehension tworzy kolekcję.
- Dictionary comprehension tworzy kolekcję.
- Generator expression tworzy iterator, który produkuje wartości na żądanie.
Przykładowo:
```python
[num * 2 for num in numbers]   # list
{num * 2 for num in numbers}   # set
(num * 2 for num in numbers)   # generator
```

Nawiasy okrągłe nie oznaczają tutaj tuple. Kontekst składniowy decyduje o tym, że jest to generator expression.

I tak, trzeba się tego nauczyć. Nie jest to najbardziej intuicyjna część składni Pythona.

4. Po co istnieje iter(), skoro mamy generatory?
To bardzo dobre pytanie. Kluczowe jest zrozumienie, że iterable i iterator to dwie różne role.

iter() nie służy wyłącznie do tworzenia generatorów.

Przykład:
```python
numbers = [10, 20, 30]
iterator = iter(numbers)
next(iterator)  # 10
next(iterator)  # 20
```

Lista jest iterable, ale nie jest iteratorem.

iter() pobiera z niej iterator, który śledzi aktualną pozycję.

Porównaj:
| Obiekt | Iterable | Iterator |
| - | - | - |
| list | Tak	| Nie |
| tuple	| Tak | Nie |
| set	| Tak | Nie |
| dict | Tak | Nie |
| Generator | Tak | Tak |
| iter(list) | Tak | Tak |

Generator jest już iteratorem, więc nie potrzebuje dodatkowego iter(), aby używać next().
Dlaczego for działa bez iter()?
Ponieważ Python wykonuje tę konwersję automatycznie.

W uproszczeniu:
```python
for num in numbers:
    print(num)
```

działa podobnie do:
```python
iterator = iter(numbers)
while True:
    try:
        num = next(iterator)
    except StopIteration:
        break

  print(num)
```

To właśnie protokół iteratora, który już poznałeś.

5. Generator expression vs generator function
| Generator expression | Generator function |
| - | - |
| Krótka składnia | Pełna definicja funkcji |
| Dobra do prostych transformacji i filtracji | Dobra do bardziej złożonej logiki |
| Nie wymaga yield | Wymaga yield |
| Jedno wyrażenie	| Dowolny blok instrukcji |
| Zwraca generator | Wywołanie zwraca generator |

Przykład tego samego zadania:

Generator expression:
```python
squares = (num ** 2 for num in numbers if num % 2 == 0)
```

Generator function:
```python
def generate_squares(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num ** 2
```

Oba rozwiązania produkują wartości w ten sam sposób: na żądanie.

Jedna korekta terminologiczna: generator function nie tyle zwraca obiekt generatora poprzez return, ile wywołanie funkcji generatorowej tworzy ten obiekt. Właściwe wykonanie rozpoczyna się dopiero przy pobieraniu wartości.