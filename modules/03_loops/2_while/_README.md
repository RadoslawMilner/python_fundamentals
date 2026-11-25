## Module 03 — Loops: while
Do tej pory używaliśmy for, kiedy mieliśmy kolekcję lub określony zakres iteracji.

while działa trochę inaczej: wykonuje kod tak długo, jak długo warunek jest prawdziwy.
1. Teoria
Podstawowa konstrukcja

```python
counter = 0

while counter < 5:
    print(counter)
    counter += 1
```

Przebieg:
| Iteracja | Counter | Warunek |
| - | - | - |
| 1 |	0 |	True
| 2	| 1	| True
| 3	| 2	| True
| 4	| 3	| True
| 5	| 4	| True
| Koniec | 5 | False

Ważne: musisz zadbać o zmianę stanu, która ostatecznie zakończy pętlę. W przeciwnym razie powstanie infinite loop.
break i continue
Działają identycznie jak w for.
- break — kończy pętlę.
- continue — przechodzi do kolejnej iteracji, ponownie sprawdzając warunek.

while vs for

| for | while |
| - | - |
| Iteruje po kolekcji |	Iteruje na podstawie warunku
| Dobrze sprawdza się przy znanej liczbie elementów	| Dobrze sprawdza się przy nieznanej liczbie iteracji
| Automatycznie przechodzi do kolejnego elementu | Sam zarządzasz zmianą stanu

for ... else i while ... else
Python ma ciekawą konstrukcję: else po pętli.

Wykonuje się ona, kiedy pętla zakończy się normalnie, czyli bez break.

```python
for number in [1, 2, 3]:
    print(number)
else:
    print("Loop completed")
```
Jeżeli dodasz break, blok else nie zostanie wykonany.

To szczególnie przydatne przy wyszukiwaniu elementów.