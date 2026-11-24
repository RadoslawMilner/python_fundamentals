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

