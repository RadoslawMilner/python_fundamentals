## Module 07 — Iterators & Generators

To jeden z ważniejszych modułów w kontekście Data Engineering. Wprowadzimy mechanizm, który pozwala przetwarzać dane element po elemencie, bez konieczności ładowania całej kolekcji do pamięci.

Zaczniemy od iteratorów.

1. Iterable vs Iterator
To dwa różne pojęcia.

Iterable — obiekt, po którym można iterować.

Przykłady:
- list
- tuple
- str
- dict
- set
Iterator — obiekt, który dostarcza kolejne elementy i pamięta, gdzie zakończył poprzednie pobieranie.

Sprawdźmy:
```python
numbers = [10, 20, 30]
iterator = iter(numbers)
```

iter() pobiera iterator z iterable.

Teraz:
```python
next(iterator)  # 10
next(iterator)  # 20
next(iterator)  # 30
```

Każde wywołanie next() przesuwa iterator do kolejnego elementu.

Kiedy elementów zabraknie:
next(iterator)

Python zgłosi StopIteration.

To nie jest błąd w działaniu iteratora. To standardowy sygnał, że nie ma już kolejnych elementów.

2. Jak działa pętla for?
To bardzo ważne.

Kiedy piszesz:
```python
for num in numbers:
    print(num)
```

Python wewnętrznie wykonuje mechanizm odpowiadający:
```python
iterator = iter(numbers)
while True:
    try:
        num = next(iterator)
    except StopIteration:
        break

print(num)
```

Czyli for automatycznie obsługuje iterator i StopIteration.

Nie musisz tego robić ręcznie.

3. Iterator jest stanowy
To kluczowa właściwość.
```python
numbers = [10, 20, 30]
iterator = iter(numbers)
next(iterator)  # 10
next(iterator)  # 20
```

Jeśli teraz ponownie użyjesz tego samego iteratora:
```python
for num in iterator:
    print(num)
```

otrzymasz tylko:
30

Dlaczego? Ponieważ iterator pamięta aktualną pozycję.

Po wyczerpaniu iteratora nie można go ponownie uruchomić. Trzeba utworzyć nowy:
```python
iterator = iter(numbers)
```