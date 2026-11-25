# Module 04.4 - Functions: Composition & Scope

# Exercise 33 - Function Composition
def calculate_subtotal(price, quantity):
    return price * quantity

calculate_subtotal(100, 3)
# 300

def calculate_discount(subtotal, discount):
    return subtotal * (1 - discount)

calculate_discount(calculate_subtotal(100, 3), 0.1)
# 270.0

def calculate_total(discount_amount, shipping):
    return discount_amount + shipping
    # due to calculated discount_amount the subtotal is more than needed - I removed it

calculate_total(calculate_discount(calculate_subtotal(100, 3), 0.1), 15)
# 285.0

def calculate_order(price, quantity, discount, shipping):
    subtotal = calculate_subtotal(price, quantity)
    discount_amount = calculate_discount(subtotal, discount)
    return calculate_total(discount_amount, shipping)

calculate_order(100, 3, 0.1, 15)
# 285.0

# Exercise 34 - Early Return
def validate_user(username, password, is_active):
    if not username or not isinstance(username, str) or not username.strip():
        return "Missing username"
    if not password or not isinstance(password, str) or not password.strip():
        return "Missing password"
    if not is_active or not isinstance(is_active, bool):
        return "Account inactive"
    return "Valid user"

validate_user('','','')
# 'Missing username'
validate_user(' ',' ',' ')
# 'Missing username'
validate_user('name',123,' ')
# 'Missing password'
validate_user('name','123',' ')
# 'Account inactive'
validate_user('name','123',123)
# 'Account inactive'
validate_user('name','123',False)
# 'Account inactive'
validate_user('name','123',None)
# 'Account inactive'
validate_user('name','123',True)
# 'Valid user'

# Exercise 35 - Type Hints
def calculate_total(price: float,quantity: int) -> float | None:
    return price * quantity

# nie, nie wymusi. tego faktu juz sie nauczylem w exercise 34. besides, w docs jest napisane: 
# "Note The Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as type checkers, IDEs, linters, etc."
# troche... szkoda. szalenie podoba mi sie fakt, ze konwencja pythona wskazuje na pisanie takich elementow - metoda jest DUUUUUZO bardziej readable. A nie trzeba uzywac komentarzy.
# IMO? z Rubiego? Dla mnie to ogromny plus. Natomiast, mialem nadzieje ze jest cos wbudowanego w samego pythona, co by sprzęzało taki dokładny opis z guard against data.
# a jestem ciekaw dlaczego. poniewaz wciez, dwukropka po funkcji - syntax jest guarded bardzo (IMO kolejny plus, eliminuje juz mase potencjalnych silly bugow)

calculate_total(10, 3)
# 30
calculate_total('string', 'niewime3')
# Traceback (most recent call last):
#   File "<python-input-77>", line 1, in <module>
#     calculate_total('string', 'niewime3')
#     ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
#   File "<python-input-73>", line 5, in calculate_total
#     return price * quantity
#            ~~~~~~^~~~~~~~~~
# TypeError: can't multiply sequence by non-int of type 'str'

# Exercise 36 - Docstrings
def calculate_average(numbers: list[int | float]) -> float:
    """Calculate average

    Args:
      numbers: List with numbers

    Returns:
      None for invalid data or empty list.
      Float average value for valid data.
    """
    if not numbers or not isinstance(numbers, list):
      return None
    total = 0
    for num in numbers:
      total += num
    return total / len(numbers)

numbers = [1,2,3,3,4,5,6]
calculate_average(numbers)
# 3.4285714285714284
