print("Task Date: 2.10.2023")
print("Task 3:\n")

"""
Напишіть програму для сортування списку методом
удосконаленого бульбашкового сортування. Удосконалення
полягає в тому, щоб аналізувати кількість перестановок на
кожному кроці. Якщо ця кількість дорівнює нулю, то продовжувати сортування немає сенсу — список відсортовано.
"""


def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                # Swap elements
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        # if no swaps are made in this pass, the list is already sorted
        if not swapped:
            break

    return lst


# main
my_list = [5, 8, 2, 1, 9, 4, 7, 6, 3]
sorted_list = bubble_sort(my_list)
print(sorted_list)