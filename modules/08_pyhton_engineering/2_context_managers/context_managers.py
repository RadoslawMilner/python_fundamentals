# Module 08.2 — Context Managers

# Exercise 101 - Understanding the execution order
class Resource:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")


resource = Resource()

with resource as item:
    print("Inside context")

# Nie uruchomilem kodu

# 101.1
# Entering context
# Inside context
# Exiting context

# 101.2
# metoda '__enter__()' zwraca wartosc, przypisywana do zmiennej po 'as'. 
# metoda ta znajduje sie w klasie 'Resource'. Zostala utworzona instancja klasy w zmiennej 'resource'
# item to wartosc zwrocona przez 'resource.__enter__()'

# IMPORTANT !!!
# 'as item' nie przypisuje automatycznie obiektu context managera. Przypisuje wynik __enter__().

# 101.3
# tak. poniewaz '__exit__()' otrzymuje informacje o wyjatku jesli tak nastapi. ValueError jest wyjatkiem.
# co wiecej, jest nawet wyposazony aby przyjac taki wyjatek. 
# Na koniec moze zadecydowac, czy taki wyjatek propagowac dalej.

# Exercise 102 — Exception lifecycle

class Resource:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        print(exc_type)
        print(exc_value)
        print(traceback)

resource = Resource()

with resource as item:
    print("Inside context")
    raise ValueError("Invalid transaction")

print("After context")

# Nie uruchomilem kodu

# 102.1
# Entering context
# Inside context
# Exiting context
# <class 'ValueError'>
# Invalid transaction
# <traceback object>

# 102.2
# Czy After context zostanie wykonane?
# Nie.
# Nie chodzi wyłącznie o to, że instrukcja znajduje się poza with.

# Chodzi o to, że:
# 1. Wewnątrz with występuje ValueError.
# 2. Python wywołuje __exit__().
# 3. __exit__() zwraca domyślnie None.
# 4. Wyjątek nie zostaje stłumiony.
# 5. Python propaguje wyjątek dalej.
# 6. Normalny przepływ programu zostaje przerwany.

# 102.3
# exc_type - <class 'ValueError'> - Klasa wyjątku
# exc_value - Invalid transaction - Instancja wyjątku
# traceback - obiekt przechowujący informacje o stosie wywołań w momencie wystąpienia wyjątku. - Obiekt stosu wywołań

# 102.4
# Python przekazuje informację o wyjątku do __exit__(), dając mu możliwość jego obsłużenia lub stłumienia.

# Exercise 103 — Exception suppression
class Resource:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

        if exc_type is ValueError:
            return True


resource = Resource()

with resource as item:
    print("Inside context")
    raise ValueError("Invalid transaction")

print("After context")

# nie uruchomilem kodu

# 103.1
# tak, poniewaz tym razem, blad przerywajacy program, zostaje stlumiony, za pomoca boolean true, zwroconego przez __exit__

# 103.2
# nie, poniewaz tym razem funkcja __exit__ po prostu zwraca boolean true.

# 103.3
# poniewaz exc_value zwroci nam 'Invalid transaction'

# 103.4
# wyjatek nie zostanie stlumiony, poniewaz warunek bedzie false, wiec nie zwroci true na koncu. zatem exit bedzie propagowal wyjatek.
# zatem program zostanie zatrzymany.

# nie uruchomilem kodu

# pytanie dot. dziedziczenia wyjatkow.
# warunek nie powinien byc prawdziwy. owszem InvalidTransactionError dziedziczy po FinancialError, 
# # lecz wciaz jest inna klasa, mogaca zawierac kolejne dzieci/metody. Ba funkcje nadpisujace znajdujace sie w parent.
# 
# Exercise 104
class FinancialError(Exception):
    pass

class InsufficientFundsError(FinancialError):
    pass

class InvalidTransactionError(FinancialError):
    pass

class InvalidCurrencyError(InvalidTransactionError):
    pass

def __exit__(self, exc_type, exc_value, traceback):
    print("Exiting context")

    if issubclass(exc_type, FinancialError):
        return True

# Exercise 105 — Resource Lifecycle Management
class Connection:
    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()

    def connect(self):
        print('Connecting...')

    def disconnect(self):
        print('Disconnecting...')

    def fetch_data(self):
        print('Fecthing financial data...')

with Connection() as connection:
    connection.fetch_data()

# Connecting...
# Fetching financial data...
# Disconnecting...

# A. Lifecycle ownership
# Klasa Connection odpowiada za cały cykl życia połączenia.
# Kod korzystający z połączenia nie musi wiedzieć, jak je zamknąć.
# To separacja odpowiedzialności:
# - użytkownik obiektu wykonuje operacje;
# - context manager zarządza zasobem.
# B. Exception safety
# disconnect() powinno wykonać się również po wyjątku. Przykładowo:
# with Connection() as connection:
    # connection.fetch_data()
    # raise ValueError("Invalid data")

# Mimo wyjątku Python wywoła __exit__().
# __exit__() nie gwarantuje, że samo zamknięcie połączenia się powiedzie. Gwarantuje próbę wykonania metody sprzątającej.

# Exercise 106 — Exception during resource usage
with Connection() as connection:
    connection.fetch_data()
    raise ValueError("Invalid financial data")

print("Program continues")

# Nie uruchomilem kodu

# 106.1 - Przewidź dokładny output:
# Connecting...
# Fetching financial data...
# Disconnecting...
# Następnie Python wyświetli traceback zakończony: ValueError: Invalid financial data

# 106.2 - Czy disconnect() zostanie wykonane?
# Yes. After all __exit__() is still a function.
# I has to done, what it has in its block. 
# Python calls this exit method and pass its info about exception
# If the exception occures and if it won't be suppressed.

# 106.3 - Czy print("Program continues") zostanie wykonane?
# No. Because the program will stop in this case, due to occurring propagating an exception.

# 106.4 - Czy __exit__() zwróci None, True czy False?
# None. Disconnect and the exit do not return anything.

# 106.5 - Czy wyjątek zostanie stłumiony?
# No.

# Przepływ wykonania
# 1. Wywołanie __enter__()
# 2. Wykonanie operacji
# 3. Występuje ValueError
# 4. Python wywołuje __exit__()
# 5. Wykonuje się disconnect()
# 6. __exit__() zwraca None
# 7. Wyjątek propaguje dalej

# Exercise 107 — Failure during cleanup
class Connection:
    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()

    def connect(self):
        print("Connecting...")

    def disconnect(self):
        print("Disconnecting...")
        raise RuntimeError("Failed to disconnect")

    def fetch_data(self):
        print("Fetching financial data...")


with Connection() as connection:
    connection.fetch_data()

print("Program continues")

# 107.1 Przewidź output:
# Connecting...
# Fetching financial data...
# Disconnecting...
# Next Python will display traceback ending with: RuntimeError: Failed to disconnect

# 107.2 Czy Program continues zostanie wykonane?
# exc_type, exc_value, traceback beda none. poniewaz podczas wykonanywania samej operacji, nie wystepuje exception.
# Python nadal zarządza wykonaniem protokołu context managera. Wywołał __exit__() zgodnie z protokołem. Jednak wyjątek powstały wewnątrz __exit__() przerywa wykonanie tej metody.
# Python nie wywołuje ponownie __exit__() w celu obsłużenia tego nowego wyjątku.

# 107.3 Który wyjątek zostanie zgłoszony: RuntimeError czy żaden?
# RuntimeError

# 107.4 — Czy pierwotny wyjątek zostanie zachowany? (chodzi o wyjątek występujący wewnątrz bloku with)
# Scenariusz A — wyjątek podczas operacji
# with Connection() as connection:
#     connection.fetch_data()
#     raise ValueError("Invalid data")

# Scenariusz B — wyjątek podczas cleanup
# def disconnect(self):
    # raise RuntimeError("Failed to disconnect")

# Scenariusz C — oba wyjątki jednocześnie
# with Connection() as connection:
    # raise ValueError("Invalid data")

# A podczas wykonywania __exit__() metoda disconnect() zgłasza RuntimeError.
# W scenariuszu C pojawia się ważny mechanizm Pythona: exception chaining, a dokładniej __context__.
# Python zachowuje informację o pierwotnym wyjątku, nawet jeśli podczas obsługi tego wyjątku wystąpi kolejny.
# To nawiązuje bezpośrednio do Exercise 100, w którym poznaliśmy raise ... from ....

# Exercise 108 — Two exceptions, one context manager
class Connection:
    def __enter__(self):
        print("Connecting...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Disconnecting...")
        raise RuntimeError("Failed to disconnect")

    def fetch_data(self):
        print("Fetching data...")


with Connection() as connection:
    connection.fetch_data()
    raise ValueError("Invalid financial data")

print("Program continues")

# nie uruchomilem kodu

# 108.1 - Jaki wyjątek będzie końcowym, propagowanym wyjątkiem?
# W bloku with występuje ValueError.
# Python wywołuje __exit__(), przekazując informacje o ValueError.
# __exit__() rozpoczyna cleanup.
# jest zgłaszany RuntimeError.
# Nowy wyjątek propaguje dalej.
# Końcowym wyjątkiem jest RuntimeError.

# 108.2 - Czy ValueError całkowicie znika, czy Python zachowuje o nim informację?
# Python zachowuje pierwotny wyjątek jako kontekst nowego wyjątku.
runtime_error.__context__  # ValueError instance
# IMPORTANT!!! __context__ przechowuje instancję wyjątku, nie samą klasę.
# Ponadto Python domyślnie wyświetli oba wyjątki w tracebacku, używając komunikatu:
# During handling of the above exception, another exception occurred:

# 108.3 — Rola __context__
# Poprawnie, ale dodajmy istotne rozróżnienie.
# Atrybut	      |   Znaczenie
# __context__	  |   Poprzedni wyjątek podczas obsługi którego wystąpił nowy
# __cause__	    |   Wyjątek jawnie wskazany przez raise ... from ...

runtime_error.__context__  # ValueError
runtime_error.__cause__    # None
# Nie użyliśmy raise ... from ..., więc nie ustawiliśmy jawnej przyczyny.

# 108.4 — Program continues
# Poprawnie.
# RuntimeError nie został obsłużony, więc program nie przechodzi do następnej instrukcji.

# Exercise 109 — Context Manager vs Exception Chaining
# wariant A:
def __exit__(self, exc_type, exc_value, traceback):
    raise RuntimeError("Cleanup failed")

# wariant B:
def __exit__(self, exc_type, exc_value, traceback):
    raise RuntimeError("Cleanup failed") from exc_value

# 109.1 - Czy w obu wariantach końcowym wyjątkiem będzie RuntimeError?
# tak.

# 109.2 - Jaka jest różnica pomiędzy __context__ i __cause__ w tych wariantach?
# Wyjątek z jawnym łańcuchem w polu __cause__ jest zawsze wyświetlany, jeśli występuje. w tym przypadku 'raise ... from...'
# Wyjątek z niejawnym łańcuchem w polu __context__  (raise...) jest wyświetlany tylko wtedy, gdy __cause__ ma wartość None, a __suppress_context__ ma wartość false.

# Właściwość           |	Wariant A   | 	Wariant B
# __context__          |	ValueError  | 	ValueError
# __cause__	           |  None	      |   ValueError
# __suppress_context__ |	False	      |   True
# Jawne powiązanie	   |  Nie	        |   Tak

# IMPORTANT !!! w wariancie B __context__ nadal przechowuje pierwotny wyjątek.
# raise ... from ... nie usuwa go. Ustawia natomiast jawny __cause__ i __suppress_context__ = True.

# 109.3 - Czy raise ... from ... zmienia kolejność propagowania wyjątków, czy przede wszystkim sposób opisywania ich relacji?
# raise ... from ... zmienia sposób określenia relacji pomiędzy wyjątkami, a nie podstawowy mechanizm propagacji.

# Exercise 110 — Understanding @contextmanager
from contextlib import contextmanager

@contextmanager
def connection():
    print("Connecting...")

    yield "Database connection"

    print("Disconnecting...")


with connection() as conn:
    print(conn)

# nie uruchomilem kodu

# 110.1 predicted output
# Connecting...
# Database connection
# Disconnecting...

# 110.2 what will be assign to 'conn'?
# yield "Database connection" -> przekazuje tę wartość do zmiennej conn.
# Czyli:
# conn = "Database connection"

# 103.3 yield vs return
# Zwykły generator:
def numbers():
    yield 1
    yield 2
    yield 3

# Po pierwszym yield generator nie kończy działania.
# Zostaje zawieszony w aktualnym miejscu. Zachowuje swój stan lokalny i może wznowić wykonanie przez next().
# W @contextmanager wykorzystujemy dokładnie tę właściwość.

# Porównaj:
# return
def example():
    print("Before")
    return 10
    print("After")  # unreachable

# Funkcja kończy wykonanie.

# yield
def example():
    print("Before")
    yield 10
    print("After")

# Funkcja zawiesza wykonanie i może zostać wznowiona.

# 110.4 — Co dzieje się po zakończeniu with?
# Tutaj dochodzimy do najważniejszego mechanizmu.

# Sekwencja:
# 1. Python rozpoczyna wykonywanie generatora.
# 2. Generator wykonuje print("Connecting...").
# 3. Generator dociera do yield.
# 4. Zwraca "Database connection" do zmiennej conn.
# 5. Wykonywany jest blok with.
# 6. Po opuszczeniu bloku Python wznawia generator.
# 7. Generator wykonuje print("Disconnecting...").
# 8. Generator kończy działanie.
# To właśnie stanowi podstawę @contextmanager.

# Exercise 111 — Generator state and context managers
from contextlib import contextmanager

@contextmanager
def transaction():
    print("BEGIN")

    yield "transaction_id_123"

    print("COMMIT")


with transaction() as tx:
    print(f"Processing {tx}")

print("Finished")

# nie uruchomilem kodu

# 111.1 Przewidź dokładny output.
# BEGIN
# Processing transaction_id_123"
# COMMIT
# Finished

# 111.2 W którym momencie generator zostaje zawieszony?
# Po zwroceniu "transaction_id_123" do tx

# 111.3 Kto wznawia jego wykonanie?
# Zakończenie bloku with powoduje, że context manager wznawia generator.
# Technicznie robi to mechanizm contextlib, który zarządza iteracją generatora.

# 111.4 Czy COMMIT wykona się, jeżeli wewnątrz with wystąpi ValueError?

# Jeżeli wewnątrz bloku wystąpi nieobsłużony wyjątek, contextlib wznowi generator, przekazując mu ten wyjątek w miejscu yield.
# Czyli nasz generator:
@contextmanager
def transaction():
    print("BEGIN")

    yield "transaction_id_123"

    print("COMMIT")

# zachowuje się tak, jakby wyjątek został zgłoszony bezpośrednio w miejscu yield.

# W konsekwencji:
# - generator zostaje wznowiony;
# - wyjątek zostaje zgłoszony w miejscu yield;
# - instrukcja print("COMMIT") nie zostaje wykonana;
# - wyjątek propaguje dalej.

# 111.5 Czy ten context manager samodzielnie obsługuje wyjątki?
# Generator otrzymuje wyjątek w miejscu yield, ale sam z siebie go nie obsługuje.
# Może natomiast użyć:
# - try/except — obsługa wyjątku;
# - finally — gwarantowane wykonanie cleanup;
# - raise — ponowna propagacja wyjątku.

# Exercise 112 — Exception injection into generator
from contextlib import contextmanager

@contextmanager
def transaction():
    print("BEGIN")

    try:
        yield "transaction_id_123"
        print("COMMIT")

    except ValueError:
        print("ROLLBACK")


with transaction() as tx:
    print(f"Processing {tx}")
    raise ValueError("Invalid transaction")

print("Finished")

# nie uruchomilem kodu

# 112.1 predict output:
# BEGIN
# Processing transaction_id_123
# ROLLBACK
# Finished

# 112.2 W którym miejscu generator otrzymuje ValueError?
# Przebieg:
# 1. Generator wykonuje się do yield.
# 2. Zwraca wartość do tx.
# 3. Generator zostaje zawieszony.
# 4. Blok with wykonuje operacje.
# 5. Występuje ValueError.
# 6. contextlib wznawia generator, wstrzykując wyjątek w miejscu yield.
# Technicznie odbywa się to przy użyciu metody generatora throw().

# To bardzo istotna różnica: generator nie tylko jest wznawiany. Jest wznawiany z wyjątkiem.

# 112.3
# Ponieważ wyjątek zostaje przechwycony przez except ValueError.
# Ważne: instrukcja:
print("COMMIT")
# nie zostanie wykonana.
# Wyjątek przerywa normalny przepływ w bloku try i sterowanie przechodzi do except.

# 112.4 Czy wyjątek zostanie propagowany poza with?
# Nie.
# Po wykonaniu:
# except ValueError:
    # print("ROLLBACK")
# generator kończy działanie normalnie.
# contextlib rozpoznaje, że generator obsłużył wyjątek i zakończył się bez ponownego zgłoszenia go.
# W rezultacie wyjątek zostaje stłumiony.
# Dlatego wykonuje się:
print("Finished")


# 112.5 Zamiana except ValueError na except TypeError
# TypeError nie przechwyci ValueError.

# W konsekwencji:
# - generator zostaje wznowiony z ValueError;
# - except TypeError nie pasuje;
# - generator przerywa wykonanie;
# - contextlib propaguje wyjątek;
# - Finished nie zostanie wykonane.

# BEGIN
# Processing transaction_id_123
# Traceback (most recent call last):
  # ...
# ValueError: Invalid transaction

# Exercise 113 - uzupełnienie poniższej implementacji:
from contextlib import contextmanager

@contextmanager
def transaction():
    print("BEGIN")

    try:
        yield "transaction_id_123"

    except ValueError:
        print("ROLLBACK")
        raise

    else:
        print("COMMIT")

    finally:
        print("Finished")

with transaction() as tx:
    print(f"Processing {tx}")
    raise ValueError("Invalid transaction")

# output: 
# BEGIN
# Processing transaction_id_123
# ROLLBACK
# Finished
# Traceback (most recent call last):
#   File "<python-input-22>", line 3, in <module>
#     raise ValueError("Invalid transaction")
# ValueError: Invalid transaction

# Exercise 114 — Execution order
# Przeanalizuj:
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

class Cache:
    def __enter__(self):
        print("Opening cache")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing cache")

from contextlib import ExitStack

with ExitStack() as stack:
    db = stack.enter_context(Database())
    api = stack.enter_context(APIConnection())

    print("Processing data")

    cache = stack.enter_context(Cache())
    print("Updating cache")

# predicted output:

# Opening database
# Connecting to API
# Processing data
# Opening cache
# Updating cache
# Closing cache
# Disconnecting from API
# Closing database

# odpalilem w terminalu - ten sam result. nice! super.

# Exercise 115 — Dynamic resource management
class DataSource:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Connecting to {self.name}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Disconnecting from {self.name}")

    def fetch(self):
        print(f"Fetching from {self.name}")

from contextlib import ExitStack

sources = ["exchange_api", "inflation_api", "bank_api"]
connections = []

with ExitStack() as stack:
    # ExitStack rejestruje metodę __exit__() danego obiektu.
    for source in sources:
        ds = DataSource(source)
        connection = stack.enter_context(ds) # wywołuje ds.__enter__().
        # Zwrócona wartość trafia do connection.
        connections.append(connection)
        # connections przechowuje uzyskane instancje.

    for connection in connections:
        connection.fetch()
# Po zakończeniu bloku with ExitStack wywołuje zarejestrowane metody __exit__() w kolejności LIFO.

# output:
# Connecting to exchange_api
# Connecting to inflation_api
# Connecting to bank_api
# Fetching from exchange_api
# Fetching from inflation_api
# Fetching from bank_api
# Disconnecting from bank_api
# Disconnecting from inflation_api
# Disconnecting from exchange_api

# Exercise 116 - Conditional resource acquisition
sources = {
    "exchange_api": True,
    "inflation_api": False,
    "bank_api": True
}
with ExitStack() as stack:
    connections = []

    for key, value in sources.items():
        if value:
            ds = DataSource(key)
            connection = stack.enter_context(ds)
            connections.append(connection)

    for connection in connections:
        connection.fetch()

# Connecting to exchange_api
# Connecting to bank_api
# Fetching from exchange_api
# Fetching from bank_api
# Disconnecting from bank_api
# Disconnecting from exchange_api

# ExitStack jest nie tyle wygodniejszy w tym przypadku co wrecz dowozi to, do czego/dlaczego zostal stworzony:
# - dynamiczna liczba zasobów. przeciez mozna modyfikowac liste/dictionary
# - zasoby są dodawane warunkowo - dokładnie.
# - zarządzamy wieloma zasobami w jednym miejscu. ponownie, nic dodac.

# Exercise 117 - Exception during resource acquisition
class DataSource:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Connecting to {self.name}")

        if self.name == "bank_api":
            raise ConnectionError("Bank API unavailable")

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Disconnecting from {self.name}")

    def fetch(self):
        print(f"Fetching from {self.name}")

from contextlib import ExitStack

sources = [
    "exchange_api",
    "inflation_api",
    "bank_api"
]

with ExitStack() as stack:
    connections = []

    for source in sources:
        ds = DataSource(source)
        connection = stack.enter_context(ds)
        connections.append(connection)

    for connection in connections:
        connection.fetch()

# predicted outcome:
# Connecting to exchange_api
# Connecting to inflation_api
# Connecting to bank_api
# ConnectionError: "Bank API unavailable"
# Fetching from exchange_api
# Fetching from bank_api
# Disconnecting from bank_api
# Disconnecting from inflation_api
# Disconnecting from exchange_api
# opusci ConnectionError

# which is wrong

# correct one:
# Connecting to exchange_api
# Connecting to inflation_api
# Connecting to bank_api
# Disconnecting from inflation_api
# Disconnecting from exchange_api
# Traceback (most recent call last): ConnectionError: Bank API unavailable

# Dlaczego bank_api.__exit__() nie zostaje wykonane?

# 2xIMPORTANT !!!!!!!!
# ExitStack.enter_context() rejestruje metodę __exit__() dopiero po pomyślnym zakończeniu __enter__().

# bank_api.__enter__() nie kończy się poprawnie.
# W konsekwencji bank_api.__exit__() nie zostaje zarejestrowane w ExitStack.
# Natomiast dwa poprzednie zasoby zostały poprawnie zarejestrowane.
# To właśnie dlatego zostają zamknięte.

# 2xIMPORTANT !!!!!!!!

# 1. Wyjątek przerywa wykonywanie bloku with.
# 2. Python wywołuje ExitStack.__exit__().
# 3. ExitStack przechodzi przez zarejestrowane callbacki w kolejności LIFO.
# 4. Wywołuje inflation_api.__exit__().
# 5. Wywołuje exchange_api.__exit__().
# 6. Nieobsłużony ConnectionError propaguje dalej.
# To ważne rozróżnienie: cleanup nie wymaga wcześniejszego przechwycenia wyjątku.


# - bank_api.__enter__() zgłasza ConnectionError;
# - inflation_api.__exit__() zgłasza RuntimeError;
# - exchange_api.__exit__() wykonuje się normalnie.
# ExitStack nadal będzie próbował wykonać pozostałe callbacki.

# Jednak wyjątek powstały podczas cleanup może zmienić końcowy wyjątek propagowany przez stos.

# Warto to zapamiętać przy projektowaniu niezawodnych systemów.

# Exercise 118 — Multiple exceptions in ExitStack
class DataSource:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Connecting to {self.name}")

        if self.name == "bank_api":
            raise ConnectionError("Bank API unavailable")

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Disconnecting from {self.name}")

        if self.name == "inflation_api":
            raise RuntimeError("Failed to disconnect inflation API")

    def fetch(self):
        print(f"Fetching from {self.name}")

from contextlib import ExitStack

sources = [
    "exchange_api",
    "inflation_api",
    "bank_api"
]

with ExitStack() as stack:
    connections = []

    for source in sources:
        ds = DataSource(source)
        connection = stack.enter_context(ds)
        connections.append(connection)

    for connection in connections:
        connection.fetch()

# output:
# Connecting to exchange_api
# Connecting to inflation_api
# Connecting to bank_api
# Disconnecting from inflation_api
# Disconnecting from exchange_api
# Traceback (most recent call last):
#   ...
# ConnectionError: Bank API unavailable

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   ...
# RuntimeError: Failed to disconnect inflation API

# 1. Czy exchange_api.__exit__() zostanie wykonane mimo RuntimeError z inflation_api.__exit__()?
# Tak. ExitStack nie przerywa wykonywania pozostałych callbacków tylko dlatego, że jeden z nich zgłosił wyjątek.

# Kolejność:
# 1. bank_api.__enter__() zgłasza ConnectionError.
# 2. ExitStack rozpoczyna cleanup.
# 3. inflation_api.__exit__() zgłasza RuntimeError.
# 4. ExitStack nadal wykonuje exchange_api.__exit__().
# 5. Po zakończeniu cleanup propaguje końcowy wyjątek.
# Ważne: nie dlatego, że każdy __exit__() musi zawsze zostać wykonany. W tym przypadku dlatego, że ExitStack został zaprojektowany tak, aby wykonać wszystkie zarejestrowane callbacki, nawet jeśli jeden z nich zgłosi wyjątek.

# 2–4. Propagacja i __context__
# Zgadza się:
# - RuntimeError ostatecznie opuszcza ExitStack.
# - ConnectionError nie zostaje utracony.
# - Jest dostępny przez RuntimeError.__context__.
# - Python pokaże oba wyjątki w tracebacku, z informacją, że drugi wystąpił podczas obsługi pierwszego.
# __context__ zachowuje kontekst wyjątku, który był obsługiwany w momencie zgłoszenia nowego wyjątku. To mechanizm diagnostyczny, a nie osobny mechanizm propagacji.

# 5. Czy fetch() zostanie wykonane?
# Nie. Pętla fetch() nie zostanie osiągnięta, ponieważ wyjątek z enter_context() przerywa pierwszą pętlę.

# Exercise 119 - ExitStack vs nested with
class DataSource:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Connecting to {self.name}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Disconnecting from {self.name}")

    def fetch(self):
        print(f"Fetching from {self.name}")

# Analiza: Variant A - nested with:
with DataSource("exchange_api") as exchange:
    with DataSource("inflation_api") as inflation:
        with DataSource("bank_api") as bank:
            exchange.fetch()
            inflation.fetch()
            bank.fetch()

# Analiza: Variant B - ExitStack:
from contextlib import ExitStack

sources = ["exchange_api", "inflation_api", "bank_api"]

with ExitStack() as stack:
    connections = []

    for source in sources:
        connection = stack.enter_context(DataSource(source))
        connections.append(connection)

    for connection in connections:
        connection.fetch()

# 1. Czy kolejność Connecting i Disconnecting będzie identyczna w obu wariantach?
# Tak. Poniewaz dla obu wariantow jest zastosowane LIFO.

# 2. Czy kolejność fetch() będzie identyczna?
# Nested with: kolejność wynika bezpośrednio z instrukcji.
# ExitStack: kolejność wynika z iteracji po connections.

# 3. Co stanie się, jeśli bank_api.__enter__() zgłosi ConnectionError? Które zasoby zostaną zamknięte w każdym wariancie?
# W obu wariantach exchange_api i inflation_api zostaną zamknięte.
# Istotny szczegół: bank_api.__exit__() nie zostanie wywołane, ponieważ jego __enter__() nie zakończyło się sukcesem.

# 4. Jaka jest zasadnicza różnica między tymi rozwiązaniami, skoro oba zapewniają cleanup w odwrotnej kolejności?
# ExitStack nie jest po prostu bardziej abstrakcyjnym zamiennikiem with. Rozwiązuje konkretny problem — dynamiczne zarządzanie cyklem życia wielu zasobów.

# Exercise 120 — Context Managers: final checkpoint
class ManagedConnection:
    def __enter__(self):
        print('Connecting to...')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if issubclass(exc_type, ConnectionError):
            print('ROLLBACK ')

        else:
            print('COMMIT ')
        
        print('Disconnecting from...')

# Variant A - error-free
with ManagedConnection() as project:
    pass

# Variant B - error
with ManagedConnection() as project:
    raise ConnectionError
