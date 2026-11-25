# Module 05.1 — Collections

# Exercise 42 - List Operations
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers
# [10, 20, 30, 40, 50, 60]
numbers.extend([70, 80])
numbers
# [10, 20, 30, 40, 50, 60, 70, 80]
numbers.insert(1, 15)
numbers
# [10, 15, 20, 30, 40, 50, 60, 70, 80]
numbers.remove(30)
numbers
# [10, 15, 20, 40, 50, 60, 70, 80]
numbers.pop
# <built-in method pop of list object at 0x105376700>
numbers
# [10, 15, 20, 40, 50, 60, 70, 80]
numbers.pop()
# 80
numbers
# [10, 15, 20, 40, 50, 60, 70]

# Exercise 43 - List Slicing
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
first_three = numbers[:3]
# [10, 20, 30]
last_three = numbers[-3:]
# [70, 80, 90]
numbers.index(30)
# 2
numbers.index(70)
# 6
from_i2_to_i6 = numbers[2:7]
# [30, 40, 50, 60, 70]
every_second = numbers[::2]
# [10, 30, 50, 70, 90]
numbers[::1]
# [10, 20, 30, 40, 50, 60, 70, 80, 90]
list_reversed = numbers[::-1]
# [90, 80, 70, 60, 50, 40, 30, 20, 10]
every_second_reversed = numbers[::-2]
# [90, 70, 50, 30, 10]

# Exercise 44 - List Mutation vs Copy
original = [1, 2, 3]
reference = original
shallow_copy = reference.copy()
original
# [1, 2, 3]
reference
# [1, 2, 3]
shallow_copy
# [1, 2, 3]
reference.append(4)
reference
# [1, 2, 3, 4]
original
# [1, 2, 3, 4]
shallow_copy
# [1, 2, 3]
shallow_copy.append(5)
shallow_copy
# [1, 2, 3, 5]
reference
# [1, 2, 3, 4]
original
# [1, 2, 3, 4]

# original and reference are shared object. the variable reference points at the same object as the variable original. thats the aliasing.
# reference is NOT the new object
# shallow_copy is an independent, new object.
# appending 4 to reference variable, mutates lists object. thats why we see changes in reference and original. because these 2 variables share 1 object.
# appending 5 to shallow_copy variable, mutates next object.

# Exercise 45 - Remove Duplicates
numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]
new_list = []
for num in numbers:
    if num not in new_list:
      new_list.append(num)

# wpisalem sobie jako draft: "if already num in new_list". W VS code. Patrze a on podkresla mi tylko 'already'.
# wiec zlozylem pelne zdanie w po ang. gpt. nawet rubim nie mozna napisac tak idiomatycznego zdania (za wyjatkiem mockow/spec-ów z shouldą).
# do glowy by mi nie przyszlo taka prostotoa wyrazenia. dlatego szukalem po count, dokumentacji, remove, del etc.
