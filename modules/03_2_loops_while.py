# Module 03.2 — Loops: while

# Exercise 10 - Countdown
counter = 10
while counter > 0:
    print(counter)
    counter -= 1
else:
    print("Liftoff!")

# Exercise 11 - Sum Until Zero
numbers = [5, 10, 15, 0, 20, 25]
sum_until_zero = 0
index = 0
while index < len(numbers) and numbers[index] != 0:
    num = numbers[index]
    if num == 0:
        break
    sum_until_zero += num
    index += 1

print("sum_until_zero:", sum_until_zero)

# Exercise 12 - Guessing Logic
secret_number = 7
guess = 0
trials = 0
while guess != secret_number:
    guess += 1
    trials += 1

print(f"In {trials} trials.")

# Exercise 13 - Search with for else
# Exercise 15 - Repetition
numbers = [4, 8, 15, 16, 23, 42]
target = 16
for num in numbers:
    if num == target:
        print("Found")
        break
else:
    print("Not found")

# Exercise 14 - Skip and Stop
# Exercise 16 - Repetition
numbers = [2, 5, 8, 11, 14, 17, 20, 23, 26]
for num in numbers:
    if num > 20:
        break
    if num % 2 == 0:
        print(num)
        continue
