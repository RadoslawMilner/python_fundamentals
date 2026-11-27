## Module 08.2 — Context Managers: Managing multiple resources

Przechodzimy do kolejnego zagadnienia: zarządzania wieloma zasobami.

Do tej pory zarządzaliśmy jednym zasobem:
```python
with Connection() as connection:
    connection.fetch_data()
```

W rzeczywistych systemach często potrzebujemy kilku zasobów jednocześnie.

Przykładowo Financial Data Platform może korzystać z:
- połączenia z PostgreSQL;
- pliku z danymi wejściowymi;
- połączenia HTTP z API.
Każdy z tych zasobów ma własny lifecycle.

1. Problem — nested context managers
Rozważmy dwie klasy:

```python
class Database:
    def __enter__(self):
        print("Opening database")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing database")


class APIConnection:
    def __enter__(self):
        print("Connecting to API")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Disconnecting from API")
```

Możemy używać ich zagnieżdżając instrukcje / nested `with`:

```python
with Database() as db:
    with APIConnection() as api:
        print("Fetching exchange rates")
```

Output:
```
Opening database
Connecting to API
Fetching exchange rates
Disconnecting from API
Closing database
```

Ważna zasada: LIFO
Zasoby są zwalniane w odwrotnej kolejności do kolejności ich pozyskiwania.

LIFO = Last In, First Out.
Lifecycle
  1. Acquire Database
    Pierwszy otwarty zasób

  2. Acquire API
    Drugi otwarty zasób

  3. Release API
    Pierwszy zamknięty zasób

  4. Release Database
    Ostatni zamknięty zasób

Dlaczego?

Ponieważ drugi zasób może zależeć od pierwszego. Zamknięcie zasobów w odwrotnej kolejności pozwala zachować poprawny lifecycle.

2. `contextlib.ExitStack`
Python oferuje narzędzie, które upraszcza zarządzanie wieloma context managerami:

```python
from contextlib import ExitStack
```

Przykład:
```python
with ExitStack() as stack:
    db = stack.enter_context(Database())
    api = stack.enter_context(APIConnection())

    print("Fetching exchange rates")
```

Output będzie taki sam jak przy zagnieżdżonych `with`.

`ExitStack` pozwala dynamicznie dodawać context managery do jednego kontekstu.

Jego główne zastosowania:
- liczba zasobów nie jest znana z góry;
- zasoby są dodawane warunkowo;
- zarządzamy wieloma zasobami w jednym miejscu;
- potrzebujemy kontrolować kolejność ich zwalniania.
Nie musimy jeszcze znać wszystkich metod `ExitStack`. Na razie skupiamy się na lifecycle.

3. Dlaczego LIFO?
To klasyczny mechanizm stosu:
- push — dodawanie zasobu;
- pop — zdejmowanie zasobu;
- LIFO — ostatni dodany jest pierwszym usuwanym.
Jest jeszcze jedna ważna konsekwencja.

Załóżmy zależność:
```
Database
  └── Transaction
        └── Cursor
```

Nie możemy bezpiecznie zamknąć Database, kiedy Transaction i Cursor nadal korzystają z tego zasobu.

LIFO naturalnie wspiera taki model zależności.

4. Exceptions i ExitStack
Dobrze zauważyłeś, że callbacki mogą wykonywać operacje związane z obsługą wyjątków.

ExitStack nie jest jednak wyłącznie mechanizmem sprzątania.

Kolejne metody `__exit__()` mogą:
- otrzymywać informacje o wyjątku;
- tłumić wyjątki;
- propagować wyjątki;
- wpływać na informacje przekazywane kolejnym metodom `__exit__()`.
To zachowuje semantykę zagnieżdżonych instrukcji `with`.

5. Czy można używać ExitStack dla jednego zasobu?
Tak.
```python
with ExitStack() as stack:
    db = stack.enter_context(Database())
    db.fetch_data()
```

Technicznie jest to poprawne.
Jednak dla jednego znanego zasobu zwykle preferujemy:
```python
with Database() as db:
    db.fetch_data()
```

Dlaczego?

| Kryterium	| `with` | `ExitStack` |
| - | - | - |
| Jeden znany zasób |	Prostszy |	Więcej abstrakcji |
| Kilka znanych zasobów	| Bardzo dobry |	Dobry |
| Dynamiczna liczba zasobów |	Ograniczony |	Bardzo dobry |
| Warunkowe dodawanie zasobów	| Mniej wygodny |	Bardzo dobry |
| Czytelność	| Prosta struktura	| Elastyczne zarządzanie |

Nie chodzi przede wszystkim o wydajność.

Chodzi o odpowiedni poziom abstrakcji.

Zasada projektowa: nie używamy bardziej rozbudowanego narzędzia, jeżeli prostsza konstrukcja rozwiązuje problem równie dobrze.

6. Dwa poziomy zarządzania
Mamy:
- `ExitStack.__exit__()` — zarządza całym stosem zasobów.
- `DataSource.__exit__()` — zarządza pojedynczym zasobem.
To nie są te same metody.

```python
with ExitStack() as stack:
    db = stack.enter_context(Database())
    api = stack.enter_context(APIConnection())
    bank = stack.enter_context(DataSource("bank_api"))
```

Załóżmy, że `bank.__enter__()` zgłasza wyjątek.
  Execution flow
  1. `Database.enter()` -> Success -> `Database.__exit__()` zostaje zarejestrowane w ExitStack.
  2. `APIConnection.enter()` -> Success -> `APIConnection.__exit__()` zostaje zarejestrowane w ExitStack.
  3. `DataSource.enter()` -> ConnectionError -> `DataSource.__exit__()` nie zostaje zarejestrowane.
  4. `ExitStack.exit()` -> Executed -> Python opuszcza zewnętrzny blok with i wywołuje `ExitStack.__exit__()`.
  5. `APIConnection.exit()` -> Zwalnia zasób.
  6. `Database.exit()` -> Zwalnia zasób.

 Kluczowe rozróżnienie
| Metoda | Czy zostanie wykonana? |
| - | - |
| `ExitStack.__exit__()` |	Tak |
| `APIConnection.__exit__()` |	Tak |
| `Database.__exit__()`	| Tak |
| `DataSource.__exit__()`	| Nie |

Ponieważ `ExitStack.__exit__()` jest już częścią zewnętrznego bloku with. Jego wykonanie nie zależy od tego, czy wszystkie zasoby zostały poprawnie pozyskane.

Natomiast `DataSource.__exit__()` nie zostało zarejestrowane, ponieważ `DataSource.__enter__()` zakończyło się wyjątkiem.

Zapamiętaj: `ExitStack` zarządza własnym lifecycle niezależnie od powodzenia inicjalizacji każdego kolejnego zasobu.

To właśnie jest mechanizm zapewniający bezpieczeństwo wcześniej pozyskanych zasobów.

**Najważniejszy wniosek z Exercise 118:** ExitStack gwarantuje próbę wykonania wszystkich zarejestrowanych operacji cleanup. Błąd podczas jednej operacji cleanup nie blokuje pozostałych. To istotna właściwość przy zarządzaniu wieloma zasobami.