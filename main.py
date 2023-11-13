print("Task Date: 11.10.2023")
print("Task 3:\n")

"""
Створіть програму «Фірма», яка зберігає інформацію
про працівників: ПІБ, телефон, корпоративний email, назва
посади, номер кабінету, Skype. Реалізуйте можливість
додавати, вида-ляти, знаходити та змінювати дані.
Використовуйте словник для збереження інформації.
"""

# main
employees = {}

def add_employee(name, phone, email, position, room_number, skype):
    employee = {
        'name': name,
        'phone': phone,
        'email': email,
        'position': position,
        'room_number': room_number,
        'skype': skype
    }
    employees[name] = employee

def delete_employee(name):
    if name in employees:
        del employees[name]
    else:
        print(f"The employee '{name}' is not in the company.")

def search_employee(name):
    if name in employees:
        return employees[name]
    else:
        return f"The employee '{name}' is not in the company."

def update_employee(name, phone=None, email=None, position=None, room_number=None, skype=None):
    if name in employees:
        employee = employees[name]
        if phone:
            employee['phone'] = phone
        if email:
            employee['email'] = email
        if position:
            employee['position'] = position
        if room_number:
            employee['room_number'] = room_number
        if skype:
            employee['skype'] = skype
    else:
        print(f"The employee '{name}' is not in the company.")

# main
add_employee("John Doe", "555-1234", "johndoe@company.com", "Manager", 101, "johndoe_skype")
add_employee("Jane Smith", "555-5678", "janesmith@company.com", "Developer", 102, "janesmith_skype")

print(search_employee("John Doe"))  # prints J.D. info

update_employee("John Doe", phone="555-4321", skype="updated_skype")
print(search_employee("John Doe"))  # prints J.D. info

delete_employee("Jane Smith")
print(search_employee("Jane Smith"))  # The employee 'Jane Smith' is not in the company.