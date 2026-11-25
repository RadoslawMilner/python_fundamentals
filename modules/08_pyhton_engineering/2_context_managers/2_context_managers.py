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

# 101.1
# Entering context
# Inside context
# Exiting context
# <class 'ValueError'>
# Invalid transaction
# <traceback object>

# 101.2
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

# 101.3
# exc_type - <class 'ValueError'> - Klasa wyjątku
# exc_value - Invalid transaction - Instancja wyjątku
# traceback - obiekt przechowujący informacje o stosie wywołań w momencie wystąpienia wyjątku. - Obiekt stosu wywołań

# 101.4
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

# 110.2 what assign to 'conn'?
