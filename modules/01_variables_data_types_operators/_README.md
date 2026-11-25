## Module 01 — Variables, Data Types & Operators

Cel: rozumieć podstawowe typy danych i operacje w Pythonie.

Pierwsze zagadnienia:
  - int
  - float
  - str
  - bool
  - None
  - zmienne i przypisania;
  - operatory arytmetyczne;
  - operatory porównania;
  - operatory logiczne;
  - konwersje typów.

Przykładowe zadanie:
```python
price = 125.50
quantity = 4
discount = 0.15

# Calculate the final price.

final_price = (price - discount) * quantity
print(final_price)
```

solucja:
```python
final_price = price * (1 - discount) * quantity

print(final_price)  # 426.7
```