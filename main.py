print("Task Date: 1.11.2023")
print("Task 1:\n")

"""
До вже реалізованого класу «Людина» додайте конструктор та необхідні перевантажені методи.
"""

class Person:
    def __init__(self, full_name="", date_of_birth="", contact_phone="", city="", country="", home_address=""):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.contact_phone = contact_phone
        self.city = city
        self.country = country
        self.home_address = home_address

    def input_data(self):
        self.full_name = input("Enter full name: ")
        self.date_of_birth = input("Enter date of birth: ")
        self.contact_phone = input("Enter contact phone: ")
        self.city = input("Enter city: ")
        self.country = input("Enter country: ")
        self.home_address = input("Enter home address: ")

    def display_data(self):
        print("Full Name:", self.full_name)
        print("Date of Birth:", self.date_of_birth)
        print("Contact Phone:", self.contact_phone)
        print("City:", self.city)
        print("Country:", self.country)
        print("Home Address:", self.home_address)

    def update_phone(self, new_phone):
        self.contact_phone = new_phone
        print("Contact phone updated.")

    def __str__(self):
        return f"Person: {self.full_name}, {self.date_of_birth}, {self.contact_phone}, {self.city}, {self.country}, {self.home_address}"

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.full_name == other.full_name and self.date_of_birth == other.date_of_birth
        return False

# main
person1 = Person("John Smith", "01-01-1990", "123456789", "New York", "USA", "123 Main St")
person2 = Person("Jane Doe", "02-02-1995", "987654321", "Los Angeles", "USA", "456 Elm St")

print(person1)
print(person2)
print(person1 == person2)