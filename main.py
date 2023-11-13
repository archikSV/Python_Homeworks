print("Task Date: 27.09.2023")
print("Task 2:\n")

"""
Реалізуйте рекурсивну функцію, яка знаходить суму
чисел в заданому діапазоні.
"""

def recursive_sum(start, end):
    if start > end:
        return 0
    else:
        return start + recursive_sum(start + 1, end)

# main
start_num = 1
end_num = 5
result = recursive_sum(start_num, end_num)
print("Sum of numbers from", start_num, "to", end_num, "is", result)