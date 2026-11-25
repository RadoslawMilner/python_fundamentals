## Module 03 — Loops: for

Cel: nauczyć się iterować po kolekcjach i wykonywać operacje na każdym elemencie. To jeden z najważniejszych fundamentów dalszej pracy z Pythonem, szczególnie przy przetwarzaniu danych.

1. Teoria

for — iterowanie po kolekcji

  ```python
  numbers = [10, 20, 30]

  for number in numbers:
      print(number)
  ```

Python pobiera kolejno każdy element listy i przypisuje go do zmiennej number.

Przebieg:
| Iteracja | number |
| - | - |
| 1 |	10 |
| 2 |	20 |
| 3 |	30 |

Nie musisz zarządzać indeksem ani zwiększać go ręcznie.
range() — generowanie sekwencji liczb

```python
for i in range(5):
    print(i)
```

Wynik: 0, 1, 2, 3, 4.

Ważne właściwości:
  - range(5) — od 0 do 4.
  - range(2, 6) — od 2 do 5.
  - range(0, 10, 2) — 0, 2, 4, 6, 8.
Górna granica nie jest wliczana.
enumerate() — element i jego indeks

```python
names = ["Anna", "Mark", "John"]

for index, name in enumerate(names):
    print(index, name)
```

Zamiast samodzielnie zarządzać indeksem, dostajesz go razem z elementem.

Możesz też zacząć numerowanie od 1:
```python
enumerate(names, start=1)
```

break i continue
  - break — natychmiast kończy całą pętlę.
  - continue — pomija aktualną iterację i przechodzi do następnej.

Przykład:
```python
for number in range(5):
    if number == 2:
        continue
    print(number)
```
Wynik: 0, 1, 3, 4.