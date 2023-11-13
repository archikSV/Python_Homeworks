print("Task Date: 9.10.2023")
print("Task X:\n")

"""
Маємо три кортежі цілих чисел. Напишіть функцію,
яка знаходить елементи, які є у всіх кортежах.
"""

def find_common_elements(tuple1, tuple2, tuple3):
    common_elements = set(tuple1) & set(tuple2) & set(tuple3)
    return list(common_elements)

# main
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
tuple3 = (4, 5, 6, 7)

common_elements = find_common_elements(tuple1, tuple2, tuple3)
print(common_elements)