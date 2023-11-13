print("Task Date: 16.10.2023")
print("Task 3:\n")

"""
Напишіть програму, яка дозволяє користувачеві ввести
з клавіатури набір додатних (число більше нуля) чисел.
Числа необхідно накопичувати у списку. Після отримання
всіх значень програма повинна проаналізувати дані. У разі
виявлення від'ємного значення програма має згенерувати
виняток. Якщо всі значення у списку позитивні, програма
має повернути на екран суму всіх чисел списку.
Згенерований виняток має бути оброблений кодом
програми.
"""

def process_numbers():
    numbers = []

    while True:
        try:
            num = int(input("Enter a positive number (or a negative number to stop): "))
            if num < 0:
                raise ValueError("Negative number entered")
            numbers.append(num)
        except ValueError as e:
            print(f"Error: {e}")
            break

    if len(numbers) > 0:
        total = sum(numbers)
        print(f"The sum of the numbers is: {total}")

# main
process_numbers()
