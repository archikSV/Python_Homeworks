print("Task Date: 4.10.2023")
print("Task 1:\n")

"""
Напишіть програму «Довідник». Створіть два списки
цілих. Один список зберігає ідентифікаційні коди, другий —
телефонні номери. Реалізуйте меню для користувача:
■ відсортувати за ідентифікаційними кодами;
■ відсортувати за номерами телефонів;
■ вивести список користувачів з кодами та телефонами;
■ вихід.
"""

def sort_by_id_codes(id_codes, phone_numbers):
    sorted_data = sorted(zip(id_codes, phone_numbers))
    sorted_id_codes, sorted_phone_numbers = zip(*sorted_data)
    return sorted_id_codes, sorted_phone_numbers

def sort_by_phone_numbers(id_codes, phone_numbers):
    sorted_data = sorted(zip(phone_numbers, id_codes))
    sorted_phone_numbers, sorted_id_codes = zip(*sorted_data)
    return sorted_phone_numbers, sorted_id_codes

def print_directory(id_codes, phone_numbers):
    for id_code, phone_number in zip(id_codes, phone_numbers):
        print(f"ID: {id_code} \t Phone: {phone_number}")

# Sample data
id_codes = [1, 3, 2, 4]
phone_numbers = [555555, 222222, 444444, 111111]

# Main program loop
while True:
    print("\nMenu:")
    print("1. Sort by ID Codes")
    print("2. Sort by Phone Numbers")
    print("3. Print Directory")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        sorted_id_codes, sorted_phone_numbers = sort_by_id_codes(id_codes, phone_numbers)
        print_directory(sorted_id_codes, sorted_phone_numbers)
    elif choice == "2":
        sorted_phone_numbers, sorted_id_codes = sort_by_phone_numbers(id_codes, phone_numbers)
        print_directory(sorted_id_codes, sorted_phone_numbers)
    elif choice == "3":
        print_directory(id_codes, phone_numbers)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")