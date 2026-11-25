## Module 06 — Strings

Zaczniemy od właściwości, która odróżnia stringi od list.

1. String Immutability
Stringi w Pythonie są immutable — nie można zmienić ich zawartości po utworzeniu obiektu.

```python
text = "python"
text[0] = "P"  # TypeError
```

Możesz natomiast utworzyć nowy string:
```python
text = "Python"
```

To nie modyfikuje poprzedniego stringa. Zmienna text zostaje przypisana do nowego obiektu.

Porównaj z listą:
```python
numbers = [1, 2, 3]
numbers[0] = 99  # działa
```

Lista jest mutable, string immutable.

2. Indexing
Podobnie jak w listach, stringi obsługują indeksowanie:
```python
language = "Python"
language[0]   # 'P'
language[1]   # 'y'
language[-1]  # 'n'
language[-2]  # 'o'
```

Indeksy zaczynają się od zera. Ujemne indeksy liczą od końca.

3. Slicing
Składnia jest taka sama jak dla list:
```python
language = "Python"
language[0:3]  # 'Pyt'
language[:2]   # 'Py'
language[2:]   # 'thon'
language[::-1] # 'nohtyP'
```

Ogólna postać:
```python
string[start:stop:step]
```

stop nie jest uwzględniany.

4. Iteration
String jest iterable — możesz iterować po jego znakach:
```python
for char in "Python":
    print(char)
```

To będzie szczególnie ważne przy zadaniach algorytmicznych: palindrome, character frequency, anagrams i string parsing.

Przy wielokrotnym dodawaniu znaków może to prowadzić do kosztownego kopiowania danych.

W Pythonie często stosuje się alternatywę:
```python
chars = []

for char in text:
    chars.append(char)
    
result = ''.join(chars)
```

join() łączy elementy iterable w jeden string. To zazwyczaj wydajniejsze rozwiązanie dla większej liczby fragmentów.

Nie musisz jeszcze zmieniać swoich ćwiczeń. Chcę, żebyś rozumiał, dlaczego istnieje ta alternatywa.