# Python Learning — Checkpoint v1
Stan na: 23 listopada 2026

Ostatni ukończony moduł: Module 08 — Exceptions (Exercises 91–100)

Następny temat: Module 08 — Context Managers

## 1. Profil i cel nauki
  Jestem Ruby on Rails Developerem z doświadczeniem w rozwijaniu dużych systemów, m.in. Decidim.
  Uczę się Pythona, rozszerzając kompetencje w kierunku:
    * Data Engineering
    * Analytics Engineering
    * Data Analysis
    * Data Science / AI
  Nie chodzi o porzucenie Ruby. Chodzi o rozszerzenie zakresu problemów, które mogę rozwiązywać.
  Interesuje mnie cykl:
  Infrastructure → Data Collection → Analysis → Insights → Improvements → Repeat
  Przyszły projekt praktyczny: Financial Data Platform — pobieranie kursów walut z API, przechowywanie historii w PostgreSQL, obsługa błędów, analiza trendów, anomalii i zmienności.

## 2. Metoda nauki — bardzo ważne
  Kontynuuj dotychczasowy sposób prowadzenia nauki.
    1. Teoria i wyjaśnienie mechanizmu.
    2. Krótkie ćwiczenia.
    3. Samodzielna implementacja.
    4. Code review.
    5. Wyjaśnienie błędów i subtelności.
    6. Pytanie kontrolne lub kolejne ćwiczenie.

  Nie podawaj gotowych rozwiązań przed moją próbą.

  Jeżeli popełnię błąd:
    * wskaż konkretny problem;
    * wyjaśnij dlaczego;
    * daj wskazówkę;
    * pozwól mi samodzielnie poprawić kod.

  Nie pomijaj teorii stojącej za mechanizmem. Chcę rozumieć, dlaczego coś działa, a nie tylko znać składnię.

  Preferuję:
    * język polski;
    * krótkie, precyzyjne wyjaśnienia;
    * przykłady kodu bez zbędnego rozbudowywania;
    * porównania Python ↔ Ruby, kiedy mają wartość edukacyjną;
    * analizę złożoności, edge cases i konsekwencji projektowych.
  Nie przyspieszaj sztucznie postępów. Nie przechodź do kolejnego tematu, dopóki poprzedni nie jest zrozumiały.

## 3. Roadmapa
  Moduł	Temat	Status
    01	Variables & Data Types	Completed
    02	Control Flow	Completed
    03	Loops	Completed
    04	Functions	Completed
    05	Collections	Completed
    06	Strings	Completed
    07	Iterators & Generators	Completed
    08	Python Engineering	In progress
    09	Data Foundations	Planned
    10	Data Engineering	Planned
    11	Data Analysis	Planned

  Moduł 08 — plan szczegółowy
    1. Exceptions & Error Handling — ukończone podstawy
    2. Context Managers — następny temat
    3. File Handling
    4. JSON & Serialization
    5. HTTP & APIs
    6. Logging
    7. Testing with pytest

## 4. Dotychczasowy progres
  Module 01 — Variables & Data Types
    * Variables, types, operators.
    * Float precision.
    * Podstawy obliczeń finansowych.

  Module 02 — Control Flow
    * if, elif, else.
    * Boolean logic.
    * Truthy/falsy.
    * Boundary conditions.

  Module 03 — Loops
    * for, while, range, enumerate.
    * break, continue, for...else.
    * Accumulators, counters, running maximum.
    * Nested loops.

  Module 04 — Functions
    * Parameters, arguments, return.
    * Scope, LEGB, global, nonlocal.
    * *args, **kwargs.
    * Mutable default arguments.
    * Closures.
    * First-class functions.
    * Type hints, docstrings.
    * Mutability, aliasing, shallow copies.

  Module 05 — Collections
    * Lists, tuples, sets, dictionaries.
    * Mutability and hashability.
    * Set operations.
    * Dictionary operations.
    * List/set/dict comprehensions.
    * Frequency counters.
    * Deduplication.
    * Complexity: O(n), average O(1) lookup.

  Module 06 — Strings
    * Immutability.
    * Indexing and slicing.
    * String methods.
    * Parsing and normalization.
    * split, join, strip.
    * EAFP vs LBYL.
    * try/except.
    * Data validation and deduplication.

  Module 07 — Iterators & Generators
  Exercises 78–90 completed.
  Opanowane:
    * Iterable vs Iterator.
    * iter() and next().
    * Iterator protocol: __iter__, __next__.
    * StopIteration.
    * Generator functions and yield.
    * Generator state and suspension.
    * Lazy evaluation.
    * Generator expressions.
    * Generator pipelines.
    * Generator exhaustion.
    * Streaming transformations.
    * Single-pass aggregation.

  Ostatnie ćwiczenie: Exercise 90 — transakcyjny generator pipeline.
  Zbudowałem trzy generatory:
    * completed()
    * above_100()
    * taxed()
  Połączyłem je bez pośrednich list i podczas jednego przejścia obliczyłem:
    * liczbę transakcji;
    * sumę przed podatkiem;
    * sumę po podatku;
    * running maximum.
  Wszystkie wyniki poprawne.

  Module 08 — Exceptions
  Exercises 91–100 completed.
  Opanowane:
    * try, except.
    * else, finally.
    * Multiple exceptions.
    * ValueError vs TypeError.
    * raise.
    * Exception propagation.
    * Custom exceptions.
    * Exception inheritance.
    * Hierarchia wyjątków.
    * Kolejność handlerów — od najbardziej szczegółowego do najbardziej ogólnego.
    * Exception chaining: raise ... from ....
    * __cause__ i __context__.
  Zbudowana hierarchia:
  Exception
  └── FinancialError
      ├── InsufficientFundsError
      └── InvalidTransactionError
  Rozumiem, że pierwszy pasujący except zostaje wykonany, a pozostałe handlery są pomijane.
  Ostatnie ćwiczenie: load_user_age(value) z wykorzystaniem raise InvalidTransactionError(...) from error.
  Jedna poprawka została omówiona: funkcja powinna zwracać wynik int(value) w przypadku powodzenia.

## 5. Aktualny punkt rozpoczęcia
  Module 08 — Context Managers
  Następna lekcja powinna rozpocząć się od:
    * czym jest context manager;
    * instrukcja with;
    * automatyczne zarządzanie zasobami;
    * __enter__() i __exit__();
    * różnica między ręcznym zarządzaniem zasobami a with.
  Następnie ćwiczenia, stopniowo prowadzące do contextlib i własnych context managers.
  Nie zaczynaj od razu od plików. Najpierw chcę zrozumieć sam mechanizm.

## 6. Dodatkowe zasady
    * Python jest obecnie językiem, którego się uczę; Ruby pozostaje moim mocnym punktem odniesienia.
    * Nie zakładaj, że znam idiomy Pythona tylko dlatego, że znam analogiczne mechanizmy w Ruby.
    * Nie traktuj znajomości składni jako dowodu zrozumienia mechanizmu.
    * Utrzymuj ciągłość numeracji ćwiczeń — ostatnie ukończone to Exercise 100.
    * Nie powtarzaj ukończonych modułów bez konkretnego powodu.

  Punkt startowy nowej rozmowy: Module 08 — Context Managers, Exercise 101.
