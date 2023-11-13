print("Task Date: 16.10.2023")
print("Task 1:\n")

"""
Напишіть програму, яка запитує у користувача ім'я та
вік. Після отримання даних програма повинна виводити
привітання у форматі: "Привіт, {ім'я}! Твій вік — {вік}".
Обробіть виняток, що виникає при введенні некоректного
віку (вік < 0 або вік > 130), і виведіть повідомлення про
помилку. 
"""

def greet():
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    try:
        age = int(age)
        if age < 0 or age > 130:
            raise ValueError("Invalid age")
        else:
            print(f"Hello, {name}! Your age is {age}")
    except ValueError as e:
        print(f"Error: {e}")

# main
greet()