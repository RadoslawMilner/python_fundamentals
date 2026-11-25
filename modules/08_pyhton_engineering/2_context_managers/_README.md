## Module 08 — Python Engineering

Zaczynamy od mechanizmu, bez plików i bez contextlib.

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
  with open("data.txt") as file:    content = file.read()
  ```

  Ale na razie interesuje nas mechanizm, nie pliki.

  Instrukcja with korzysta z protokołu context managera.

  Obiekt musi implementować dwie metody:
  __enter__()__exit__()

  Ich odpowiedzialności:

  __enter__()
    - Uruchamiana przy wejściu do kontekstu.
    - Przygotowuje zasób.
    - Jej wartość zwracana jest przypisywana do zmiennej po as.

  __exit__()
    - Uruchamiana przy opuszczaniu kontekstu.
    - Odpowiada za sprzątanie.
    - Wykonywana również wtedy, gdy wewnątrz with wystąpi wyjątek.

## 3. Co właściwie robi Python?
  Rozważmy taki przykład:

  ```python
  with resource as item: process(item)
  ```

  W uproszczeniu Python wykonuje następującą sekwencję:
  1. Wywołuje resource.__enter__().
  2. Przypisuje zwróconą wartość do item.
  3. Wykonuje blok with.
  4. Wywołuje resource.__exit__() przy opuszczaniu bloku.

  Ważny szczegół: __exit__() otrzymuje informacje o wyjątku, jeżeli taki wystąpił.

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

  Istotna właściwość: __exit__() może zdecydować, czy wyjątek zostanie dalej propagowany.
    - Zwraca False lub None → wyjątek jest propagowany.
    - Zwraca True → wyjątek zostaje stłumiony (suppressed).

  To bardzo ważny mechanizm. Context manager nie tylko sprząta zasoby. Może również uczestniczyć w obsłudze wyjątków.

## 4. Ręczne zarządzanie vs with
  Wyobraź sobie, że musisz przygotować zasób, wykonać operację i zagwarantować jego zwolnienie.

  Bez context managera musisz samodzielnie zadbać o odpowiednią strukturę try/finally.

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

Python oferuje jednak alternatywę: contextlib.

Jest to standardowy moduł biblioteki Pythona zawierający narzędzia do tworzenia i zarządzania context managerami.

Jednym z najważniejszych jest:
```python
from contextlib import contextmanager
```

Pozwala on tworzyć context managery przy użyciu funkcji i yield, zamiast ręcznego implementowania klasy.

Zwróć uwagę na podobieństwo do generatorów, które poznaliśmy w Module 07.

To nie jest przypadkowe. @contextmanager wykorzystuje mechanizm generatorów.

2. Pierwszy przykład — teoria
```python
from contextlib import contextmanager

@contextmanager

def resource():
    print("Entering context")
    yield
    print("Exiting context")
```
Użycie:
```python
with resource():
    print("Inside context")
```

Wynik:
```python
Entering context
Inside context
Exiting context
```

Mechanizm:
1. Kod przed yield wykonuje się przy wejściu do kontekstu.
2. yield przekazuje kontrolę do bloku with.
3. Po zakończeniu bloku wykonanie generatora jest wznawiane.
4. Kod po yield wykonuje się przy opuszczaniu kontekstu.

To bardzo podobne do __enter__() i __exit__(), ale implementowane inaczej.