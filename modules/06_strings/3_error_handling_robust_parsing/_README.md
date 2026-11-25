## Module 06 — Strings: Error Handling & Robust Parsing

Dotychczas walidowaliśmy dane przed konwersją:
```python
if age.isdigit():    age = int(age)
```

To działa dla prostych przypadków. Jednak rzeczywiste dane mogą zawierać wartości takie jak:
- "32" — poprawna liczba całkowita.
- "-5" — poprawna liczba całkowita, ale isdigit() zwróci False.
- "32.5" — liczba zmiennoprzecinkowa.
- "abc" — niepoprawna liczba.
- "" — pusty string.
Właśnie dlatego warto poznać try/except.
1. Try / Except
Python pozwala wykonać operację i przechwycić wyjątek, jeśli się nie powiedzie.
```python
try:
    age = int("32")
except ValueError:
    print("Invalid age")
```

Jeżeli konwersja się powiedzie, except zostanie pominięty.

Jeżeli konwersja rzuci ValueError, wykonany zostanie blok except.

2. Else i Finally
Możemy rozszerzyć konstrukcję:
```python
try:
    age = int("32")
except ValueError:
    print("Invalid age")
else:
    print("Conversion successful")
finally:
    print("Conversion attempt finished")
```

| Blok | Kiedy się wykonuje? |
| - | - |
| try | Zawsze — próba wykonania operacji |
| except | Gdy wystąpi pasujący wyjątek |
| else | Gdy try zakończy się bez wyjątku |
| finally |	Zawsze, niezależnie od wyniku |

finally jest szczególnie przydatne przy zasobach, np. plikach czy połączeniach.

3. Konwersja zamiast wstępnej walidacji
Porównaj:
```python
if age.isdigit():
    age = int(age)
```

z:
```python
try:
    age = int(age)
except ValueError:
    continue
```

Drugie rozwiązanie pozwala wykorzystać samą operację konwersji jako test poprawności.

Nie musisz najpierw sprawdzać, czy coś jest liczbą, a potem ponownie wykonywać konwersji.

To często lepszy wzorzec w Pythonie — nazywany EAFP:

Easier to Ask Forgiveness than Permission.

Zamiast sprawdzać z wyprzedzeniem, czy operacja się powiedzie, próbujesz ją wykonać i obsługujesz ewentualny wyjątek.

Alternatywny styl to LBYL — Look Before You Leap. Przykładem jest wcześniejsze isdigit().