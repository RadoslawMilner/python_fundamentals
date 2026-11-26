## Module 08 — Python Engineering

Zaczynamy od mechanizmu, bez plików i bez `contextlib`.

## 1. Czym jest Context Manager?
  Context manager to obiekt, który zarządza wejściem i wyjściem z określonego kontekstu wykonania.

  Jego głównym zadaniem jest zagwarantowanie wykonania określonych operacji:
    - przed rozpoczęciem pracy w danym kontekście;
    - po zakończeniu pracy w danym kontekście;
    - również wtedy, gdy podczas wykonywania kodu wystąpi wyjątek.

  Przykładowe zastosowania:

  | Zasób / operacja | Co zarządzamy? |
  | - | - |
  | File | Otwarcie i zamknięcie pliku |
  | Database connection | Otwarcie i zamknięcie połączenia |
  | Database transaction | Commit lub rollback |
  | Lock | Acquire i release |
  | Temporary resources | Utworzenie i sprzątanie |

  Kluczowa koncepcja: resource lifecycle management.

## 2. Instrukcja with
  Prawdopodobnie kojarzysz już składnię:
  ```python
  with open("data.txt") as file:
      content = file.read()
  ```

  Ale na razie interesuje nas mechanizm, nie pliki.

  Instrukcja `with` korzysta z protokołu context managera.

  Obiekt musi implementować dwie metody:
  `__enter__()__exit__()`

  Ich odpowiedzialności:

  `__enter__()`
    - Uruchamiana przy wejściu do kontekstu.
    - Przygotowuje zasób.
    - Jej wartość zwracana jest przypisywana do zmiennej po as.

  `__exit__()`
    - Uruchamiana przy opuszczaniu kontekstu.
    - Odpowiada za sprzątanie.
    - Wykonywana również wtedy, gdy wewnątrz `with` wystąpi wyjątek.

## 3. Co właściwie robi Python?
  Rozważmy taki przykład:

  ```python
  with resource as item:
      process(item)
  ```

  W uproszczeniu Python wykonuje następującą sekwencję:
  1. Wywołuje `resource.__enter__()`.
  2. Przypisuje zwróconą wartość do `item`.
  3. Wykonuje blok `with`.
  4. Wywołuje `resource.__exit__()` przy opuszczaniu bloku.

  Ważny szczegół: `__exit__()` otrzymuje informacje o wyjątku, jeżeli taki wystąpił.

  Jego sygnatura:
  ```python
  __exit__(self, exc_type, exc_value, traceback)
  ```

  Parametry:
  | Parametr | Znaczenie |
  | - | - |
  | exc_type | Klasa wyjątku |
  | exc_value |	Instancja wyjątku |
  | traceback |	Informacje o miejscu wystąpienia wyjątku |

  Jeżeli wyjątek nie wystąpił, wszystkie trzy wartości są None.

  Istotna właściwość: `__exit__()` może zdecydować, czy wyjątek zostanie dalej propagowany.
    - Zwraca `False` lub `None` → wyjątek jest propagowany.
    - Zwraca `True` → wyjątek zostaje stłumiony (suppressed).

  To bardzo ważny mechanizm. Context manager nie tylko sprząta zasoby. Może również uczestniczyć w obsłudze wyjątków.

## 4. Ręczne zarządzanie vs with
  Wyobraź sobie, że musisz przygotować zasób, wykonać operację i zagwarantować jego zwolnienie.

  Bez context managera musisz samodzielnie zadbać o odpowiednią strukturę `try`/`finally`.

  Z with Python zarządza cyklem życia zasobu zgodnie z protokołem context managera.

  To nie jest wyłącznie skrócenie składni. To standaryzacja zarządzania zasobami.

# contextlib
1. Dlaczego istnieje contextlib?
Do tej pory implementowaliśmy context manager przez klasę i dwie metody:
```python
__enter__()
__exit__()
```

To klasyczny sposób implementacji protokołu.

Python oferuje jednak alternatywę: `contextlib`.

Jest to standardowy moduł biblioteki Pythona zawierający narzędzia do tworzenia i zarządzania context managerami.

Jednym z najważniejszych jest:
```python
from contextlib import contextmanager
```

Pozwala on tworzyć context managery przy użyciu funkcji i yield, zamiast ręcznego implementowania klasy.

Zwróć uwagę na podobieństwo do generatorów, które poznaliśmy w Module 07.

To nie jest przypadkowe. `@contextmanager` wykorzystuje mechanizm generatorów.

2. Najpierw ustalmy jeden model działania `@contextmanager`

Weźmy minimalny przykład:

```python
from contextlib import contextmanager

@contextmanager
def transaction():
    print("BEGIN")

    yield "transaction_id_123"

    print("COMMIT")
```

Użycie
```python
with transaction() as tx:
    print(f"Processing {tx}")
```

Sekwencja wykonania:

| Krok | Co się dzieje? |
| - | - |
| 1	 | Wywołanie `transaction()` tworzy generator |
| 2	 | `contextlib` rozpoczyna jego wykonanie |
| 3	 | Generator drukuje `BEGIN`
| 4	 | `yield` przekazuje wartość `"transaction_id_123"` |
| 5	 | Wartość trafia do `tx`
| 6	 | Generator zostaje zawieszony |
| 7	 | Wykonuje się blok `with`
| 8	 | `contextlib` wznawia generator |
| 9	 | Generator wykonuje `print("COMMIT")` |
| 10 | 	Generator kończy działanie |

Output:
```
BEGIN
Processing transaction_id_123
COMMIT
```

Najważniejsza rzecz:

`yield` w context managerze jest punktem granicznym pomiędzy wejściem do kontekstu a wyjściem z niego.
Nie jest odpowiednikiem zwykłego return

3. Jak generator otrzymuje wyjątek?

W class-based context managerze mieliśmy:
```python
def __exit__(self, exc_type, exc_value, traceback):
    ...
```
Czyli Python jawnie przekazuje trzy informacje o wyjątku.

W generatorowym context managerze mechanizm jest inny.

Rozważ:
```python
@contextmanager
def transaction():
    print("BEGIN")

    try:
        yield "transaction_id_123"
    except ValueError as error:
        print("ROLLBACK")
        raise
    else:
        print("COMMIT")
```
Zwróć uwagę na:
```python
except ValueError as error:
```

To jest dokładnie narzędzie, którego szukałeś.

`error` jest instancją wyjątku. Możesz ją analizować, tak samo jak exc_value w poprzednim modelu.

Nie musisz tworzyć żadnej dodatkowej klasy ani ponownie wywoływać `ValueError`.
Co robi `contextlib`?
Kiedy wewnątrz `with` wystąpi wyjątek, `contextlib` przekazuje go do generatora w miejscu `yield`.

W uproszczeniu:
```
with block
    |
    | ValueError occurs
    |
    v
contextlib
    |
    | injects exception at yield
    |
    v
generator
    |
    v
except ValueError as error
```

To właśnie dlatego `try`/`except` wokół `yield` może przechwycić wyjątek powstały w kodzie korzystającym z context managera.

4. Dlaczego raise bez argumentów?

Masz trzy możliwości:
| Instrukcja |	Znaczenie |
| - | - |
| `print(error)` |	Wyświetla komunikat wyjątku |
| `raise`	| Ponownie zgłasza aktualnie obsługiwany wyjątek |
| `raise ValueError("...")` |	Tworzy i zgłasza nowy wyjątek |

Nas interesuje druga możliwość.
```python
except ValueError as error:
    print("ROLLBACK")
    raise
```

Nie tworzymy nowego wyjątku. Nie musimy nawet używać zmiennej error, jeżeli nie potrzebujemy analizować jego zawartości.
Samo raise ponownie zgłasza aktualnie obsługiwany wyjątek, zachowując jego tożsamość i pierwotny kontekst tracebacka.

4. Teraz uporządkujmy output
Dla poprawionej implementacji i takiego kodu:
```python
with transaction() as tx:
    print(f"Processing {tx}")
    raise ValueError("Invalid transaction")

print("Finished")
```

Oczekiwany przebieg:
```
BEGIN
Processing transaction_id_123
ROLLBACK
Traceback (most recent call last):
  ...
ValueError: Invalid transaction
```

`Finished` nie zostanie wykonane.

W przypadku poprawnego wykonania bloku:
```python
with transaction() as tx:
    print(f"Processing {tx}")

print("Finished")
```

Output:
```
BEGIN
Processing transaction_id_123
COMMIT
Finished
```

Zauważ: traceback nie jest komunikatem generowanym przez print(). Jest generowany przez Pythona, kiedy nieobsłużony wyjątek dociera do końca przepływu wykonania.

5. @contextmanager i otwieranie bloku
Dekorator @contextmanager przekształca funkcję generatorową w context manager.

Sam dekorator nie wykonuje jeszcze kodu generatora.
Dopiero
```python
with transaction() as tx:
```
powoduje wywołanie mechanizmu wejścia do kontekstu, który uruchamia generator aż do pierwszego yield.
```
@contextmanager
       |
       v
Generator function
       |
       v
Context manager object
       |
       v
with -> __enter__()
       |
       v
Generator runs until yield
       |
       v
Execute with block
       |
       v
with -> __exit__()
       |
       v
Resume generator / inject exception
```

6. as error:
```python
except ValueError as error:
    print("ROLLBACK")
    raise
```

Zmienna `error` jest przypisana, ale nigdzie nie jest odczytywana.
Bare `raise` nie korzysta z tej zmiennej. Python zna aktualnie obsługiwany wyjątek i potrafi go ponownie zgłosić bez jawnego wskazywania instancji.
Możesz napisać:
```python
except ValueError as error:
    print(error)
    print("ROLLBACK")
    raise
```

Wtedy `error` jest wykorzystywany.
Ale jeżeli nie potrzebujesz analizować komunikatu wyjątku, jeszcze lepszy zapis to:
```python
except ValueError:
    print("ROLLBACK")
    raise
```
