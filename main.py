print("Task Date: 9.10.2023")
print("Task 3:\n")

"""
Маємо три кортежі цілих чисел. Напишіть функцію,
яка знаходить елементи, які є в кожному з кортежів і
знаходяться в кожному з них на тій самій позиції.
"""

def find_common_elements_at_same_position(tuple1, tuple2, tuple3):
    common_elements = []
    for i in range(len(tuple1)):
        if tuple1[i] == tuple2[i] == tuple3[i]:
            common_elements.append(tuple1[i])
    return common_elements

# main
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
tuple3 = (4, 5, 6, 7)

common_elements = find_common_elements_at_same_position(tuple1, tuple2, tuple3)
print(common_elements)