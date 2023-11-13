print("Task Date: 30.10.2023")
print("Task 1:\n")

"""
Реалізуйте клас «Людина». Збережіть у класі: ПІБ,
дату народження, контактний телефон, місто, країну,
домашню адресу. Реалізуйте методи класу для введення-виведення даних та інших операцій.

"""

class Person:
    def __init__(self):
        self.full_name = ""
        self.date_of_birth = ""
        self.contact_phone = ""
        self.city = ""
        self.country = ""
        self.home_address = ""

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

# main
person = Person()
person.input_data()
print("---")
person.display_data()
print("---")
new_phone = input("Enter new contact phone: ")
person.update_phone(new_phone)
print("---")
person.display_data()