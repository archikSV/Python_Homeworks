print("Task Date: 9.10.2023")
print("Task 2:\n")

"""
Маємо три кортежі цілих чисел. Напишіть функцію,
яка знаходитьелементи, які унікальні для кожного списку.
"""

def find_unique_elements(tuple1, tuple2, tuple3):
    unique_elements = set(tuple1) ^ set(tuple2) ^ set(tuple3)
    return list(unique_elements)

# main
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
tuple3 = (4, 5, 6, 7)

unique_elements = find_unique_elements(tuple1, tuple2, tuple3)
print(unique_elements)