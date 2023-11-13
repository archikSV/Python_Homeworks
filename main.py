print("Task Date: 2.10.2023")
print("Task 1:\n")

"""
Відсортуйте перші дві третини списку в порядку зростання, якщо середнє арифметичне всіх елементів більше за нуль;
якщо ні — тільки першу третину. Решту списку не сортуйте,
а розташуйте у зворотному порядку.
"""


def sort_list(lst):
    average = sum(lst) / len(lst)

    if average > 0:
        first_two_thirds = lst[:int(len(lst) * 2 / 3)]
        sorted_first_two_thirds = sorted(first_two_thirds)
        rest = lst[int(len(lst) * 2 / 3):][::-1]  # Reverse order of the rest of the list
        return sorted_first_two_thirds + rest
    else:
        first_third = lst[:int(len(lst) * 1 / 3)]
        return first_third[::-1]  # Reverse order of the first third of the list


# main
my_list = [5, 8, 2, 1, 9, 4, 7, 6, 3]
sorted_list = sort_list(my_list)
print(sorted_list)