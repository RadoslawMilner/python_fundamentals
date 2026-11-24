# Module 08.1 — Python Engineering

# Exercise 91 — Exceptions: fundament
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

safe_divide(10, 2)
# 5.0
safe_divide(10, 0)
# >>> (None)

# Exercise 92 — try, except, else, finally
def safe_convert(value):
    try:
        converted = int(value)
    except ValueError:
        return None
    else:
        return converted
    finally:
        print("Conversion attempted")

safe_convert('123')
# Conversion attempted
# 123
safe_convert('abc')
# Conversion attempted
safe_convert('-15')
# Conversion attempted
# -15

# pytanie kontrolne: tak. finally wykona sie równiez gdy 'try' zakonczy sie przez return.
# oczywiscie wtedy 'else' nie ma sensu, ale generalnie, to tak. taka jest idea/cel finally. Bezwzgledu na wynik.

# ponadto:
# Zobaczysz Cleanup, a następnie Python przekaże dalej ZeroDivisionError.
# IMPORTANT:
# finally nie oznacza więc obsługi błędu. Służy przede wszystkim do wykonywania operacji kończących, np. zwalniania zasobów.

# Exercise 93 — Multiple exceptions
def safe_convert(value):
    try:
        converted = int(value)
    except (ValueError, TypeError):
        return None
    else:
        return converted

safe_convert('123')
# 123
safe_convert('abc')
safe_convert(None)
safe_convert(12.8)
# 12

# TypeError — operacja nie jest obsługiwana dla danego typu obiektu.
# ValueError — typ argumentu jest akceptowalny, ale jego wartość jest nieprawidłowa dla danej operacji.
# Przykładowo int("999999999999999999") działa poprawnie.

# Exercise 94 — raise: samodzielne zgłaszanie wyjątków
def calculate_discount(price, discount):
    if price <= 0:
        raise ValueError("Price cannot be negative")
    if not 0 <= discount <= 1:
        raise ValueError("The discount must be between 0 and 1, inclusive")
    return price - price * discount

calculate_discount(100, 0.2)
# 80.0
calculate_discount(-100, 0.2)
# Traceback (most recent call last):
#   File "<python-input-134>", line 1, in <module>
#     calculate_discount(-100, 0.2)
#     ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^
#   File "<python-input-132>", line 3, in calculate_discount
#     raise ValueError("Price cannot be negative")
# ValueError: Price cannot be negative
calculate_discount(100, 1.5)
# Traceback (most recent call last):
#   File "<python-input-135>", line 1, in <module>
#     calculate_discount(100, 1.5)
#     ~~~~~~~~~~~~~~~~~~^^^^^^^^^^
#   File "<python-input-132>", line 5, in calculate_discount
#     raise ValueError("The discount must be between 0 and 1, inclusive")
# ValueError: The discount must be between 0 and 1, inclusive
calculate_discount(100, 0)
# 100

# return - funkcja działa do momentu return, aby zwrocic to co ma na celu zwrocic ta funkcja. return konczy funkcje.
# raise - słuzy do zwrocenia wyjatku. zatrzymuje wykonanie funkcji
# None to stala ktora mowi o braku wartosci.
# ValueError jest wyjatkiem. dzieje sie wtedy gdy funkcja lub operacja otrzymuje zla wartosc.

# Exercise 95 — Exception propagation
def calculate_discount(price, discount):
    if price <= 0:
        raise ValueError('Price must be positive')
    if not 0 <= discount <= 1:
        raise ValueError('Invalid discount')
    
    return price * (1 - discount)

def process_order(price, discount):
    return calculate_discount(price, discount) + 15

process_order(100, 0.2)
# 95.0
process_order(-100, 0.2)
# Traceback (most recent call last):
#   File "<python-input-145>", line 1, in <module>
#     process_order(-100, 0.2)
#     ~~~~~~~~~~~~~^^^^^^^^^^^
#   File "<python-input-143>", line 2, in process_order
#     return calculate_discount(price, discount) + 15
#            ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
#   File "<python-input-142>", line 3, in calculate_discount
#     raise ValueError('Price must be positive')
# ValueError: Price must be positive

# raise Wyjątek dociera do nadrzenej funkcji: Because we call process order function. this function call other one. it is a part of process order function. whole together create 1 whole execution. raise stops execution of calculate discount. which, in turn stops execution process order.

# Exercise 96 — Custom Exceptions
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError('Amount cannot be zero or negative')
    elif amount > balance:
        raise InsufficientFundsError("Insufficient funds")
    else:
        return balance - amount

withdraw(1000, 300)
# 700
withdraw(1000, 1300)
# Traceback (most recent call last):
#   File "<python-input-6>", line 1, in <module>
#     withdraw(1000, 1300)
#     ~~~~~~~~^^^^^^^^^^^^
#   File "<python-input-4>", line 3, in withdraw
#     raise InsufficientFundsError("Insufficient funds")
# InsufficientFundsError: Insufficient funds
withdraw(1000, -50)
# Traceback (most recent call last):
#   File "<python-input-7>", line 1, in <module>
#     withdraw(1000, -50)
#     ~~~~~~~~^^^^^^^^^^^
#   File "<python-input-4>", line 5, in withdraw
#     raise ValueError('Amount cannot be zero or negative')
# ValueError: Amount cannot be zero or negative

# answer to Your question: because ValueError is incorrect for the such condition: 'if amount > balance:'
# just like TypeError != ValueError. Their purposes differs. And in this case. Value is no the problem for such condition. 
# So it's error should not be used in this way. this condition ensure about proper use that function. not value per se.

# Exercise 97 — Hierarchia własnych wyjątków
# 97.1 & 97.2
class FinancialError(Exception):
    pass

class InsufficientFundsError(FinancialError):
    pass

class InvalidTransactionError(FinancialError):
    pass

# 97.3
# raise InsufficientFundsError('Insufficient Funds')
# Traceback (most recent call last):
#   File "<python-input-11>", line 1, in <module>
#     raise InsufficientFundsError('Insufficient Funds')
# InsufficientFundsError: Insufficient Funds

# raise InvalidTransactionError('Invalid Transaction')
# Traceback (most recent call last):
#   File "<python-input-12>", line 1, in <module>
#     raise InvalidTransactionError('Invalid Transaction')
# InvalidTransactionError: Invalid Transaction

# 97.4
try:
    raise InsufficientFundsError()
    # or can be use: raise InvalidTransactionError with same output
except FinancialError:
     print('financial error')
# financial error

# 97.5
try:
    raise InsufficientFundsError()
except InsufficientFundsError:
     print('insufficient funds')
# insufficient funds

# Exercise 98 — Kolejność except i hierarchia dziedziczenia
try:
    raise InsufficientFundsError('Insufficient funds')

except FinancialError:
    print('Financial error')

except InsufficientFundsError:
    print('Insufficient funds')

# Pierwszy pasujący blok except wygrywa.
# Python zgłasza InsufficientFundsError.
# Sprawdza pierwszy except.
# InsufficientFundsError jest podklasą FinancialError.
# Dopasowanie jest prawidłowe. Wykonuje pierwszy blok. Pomija wszystkie pozostałe bloki except.
# Output: Financial error

# Od najbardziej szczegółowego wyjątku do najbardziej ogólnego. Wiec powinny zostac ZAMIENIONE.
# - InsufficientFundsError obsługuje konkretny przypadek.
# - FinancialError obsługuje pozostałe błędy finansowe, które nie zostały wcześniej przechwycone.
# Możesz myśleć o tym jak o dopasowywaniu wzorców: najpierw szczegółowe warunki, na końcu ogólny fallback.

# Exercise 99 —  Kolejność except i hierarchia dziedziczenia - utrwalenie
class FinancialError(Exception):
    pass

class InsufficientFundsError(FinancialError):
    pass

class InvalidTransactionError(FinancialError):
    pass

def process_transaction(transaction_type):
    if transaction_type == "withdrawal":
        raise InsufficientFundsError("Insufficient funds")

    if transaction_type == "transfer":
        raise InvalidTransactionError("Invalid transaction")

    if transaction_type == "unknown":
        raise ValueError("Unknown transaction type")

def catch(transaction_type):
    try:
        process_transaction(transaction_type)
    except ValueError: # because at first we should check input value at all
        print('Unknown transaction type')
    except InvalidTransactionError: # because next we should check input of transaction type if its proper
        print('Invalid transaction')
    except InsufficientFundsError: # successively check amount of funds available
        print('Insufficient funds')
    except FinancialError: # at last check general financial error(s)
        print('Financial error')

transaction_type = 'withdrawal'
catch(transaction_type)
# Insufficient funds

transaction_type = 'transfer'
catch(transaction_type)
# Invalid transaction

transaction_type = 'unknown'
catch(transaction_type)
# Unknown transaction type

# Value error nie moze dziedziczyc po FinancialError. Value error jest python's built in exception. Ponadto nie powinien. 
# Value error ma obsługiwac przypadki gdy jest podana wartosc do metody ktora tam zupelnie nie pasuje.

# Exercise 100 — raise ... from ...
def load_user_age(value):
    try:
        return int(value)
    except ValueError as error:
        raise InvalidTransactionError('Invalid user age') from error
load_user_age('35')
load_user_age('abc')
# Traceback (most recent call last):
#   File "<python-input-45>", line 3, in load_user_age
#     int(value)
#     ~~~^^^^^^^
# ValueError: invalid literal for int() with base 10: 'abc'

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "<python-input-47>", line 1, in <module>
#     load_user_age('abc')
#     ~~~~~~~~~~~~~^^^^^^^
#   File "<python-input-45>", line 5, in load_user_age
#     raise InvalidTransactionError('Invalid user age') from error
# InvalidTransactionError: Invalid user age

# odpowiedz: 
# Warto zachowac OG watek w celu ulatwienia trackingu/bugfixingu.
# 'raise NewError(...) from error' rozni sie od zwykłego 'raise NewError(...)' zwracanym komunikatem:
# for: 'raise NewError(...) from error': 'The above exception was the direct cause of the following exception:'
# for: 'raise NewError(...)': 'During handling of the above exception, another exception occurred:'

# - raise NewError(...) from error — jawnie określa przyczynę (__cause__).
# - raise NewError(...) wewnątrz except — Python automatycznie zachowuje kontekst (__context__).
# - raise NewError(...) from None — ukrywa prezentację pierwotnego kontekstu w tracebacku.
