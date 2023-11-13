print("Task Date: 8.11.2023")
print("Task 4:\n")

"""
Створіть клас InformationSystem, який має атрибут data
- словник, де ключі - це імена користувачів, а значення -
список їх контактів. Реалізуйте методи класу для додавання
нових користувачів та їх контактів.
"""

class InformationSystem:
    def __init__(self):
        self.data = {}

    def add_user(self, username):
        if username not in self.data:
            self.data[username] = []

    def add_contact(self, username, contact):
        if username in self.data:
            self.data[username].append(contact)
        else:
            print(f"User '{username}' does not exist.")

# main
system = InformationSystem()

system.add_user("John")
system.add_user("Alice")

system.add_contact("John", "123456789")
system.add_contact("John", "john@example.com")
system.add_contact("Alice", "987654321")

print(system.data)

