print("Task Date: 16.10.2023")
print("Task 2:\n")

"""
Реалізуйте перше завдання через функцію. Функція
повинна приймати ім'я і вік як параметри і повертати
відформатований рядок. Перевірка коректності отриманих
даних повинна бути всередині функції. Створіть дві версії
реалізації функції:
• Перша версія не обробляє виняток всередині функції.
Уся обробка знаходиться зовні;
• Друга версія обробляє виняток усередині функції.
"""

def format_greeting(name, age):
    if age < 0 or age > 130:
        raise ValueError("Invalid age")
    else:
        return f"Hello, {name}! Your age is {age}"

def greet(name, age):
    try:
        return format_greeting(name, age)
    except ValueError as e:
        return f"Error: {e}"

def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    result = greet(name, age)
    print(result)

# main
main()