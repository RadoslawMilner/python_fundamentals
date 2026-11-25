# Module 02 — Control Flow

# Exercise 4 - Age Classification
age = 25
if age < 13:
    print("Child")
elif age <= 17:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")

# Exercise 5 - Login Validation
username = "admin"
password = "secret123"
is_account_active = True

if username == "admin" and password == "secret123" and is_account_active:
    print("Login successful")
else:
    print("Login failed")

# Exercise 6 - Number Range
number = 42
if number > 0 and number in range(1, 101) and (number % 2 == 0 or number % 3 == 0):
    print("The number is positive, within the range of 1 to 100, and is either even or divisible by 3.")

# Exercise 7 - Truthy or Falsy
value = []
if value:
    print("The value is truthy.")
else:
    print("The value is falsy.")
# for value = [] is falsy, because it is an empty list, which evaluates to False in a boolean context.
# for value = [0] is truthy, because it is a non-empty list, which evaluates to True in a boolean context.
# Despite containing a falsy value (0), the list itself is not empty, so it is considered truthy.
