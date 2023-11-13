print("Task Date: 1.11.2023")
print("Task 5:\n")

"""
Реалізуйте клас «Вебсайт». Збережіть у класі: назву
вебсайту, адресу та опис вебсайту. Реалізуйте конструктор
та методи класу для введення-виведення даних, а також
для інших операцій. Використовуйте механізм перевантаження методів.
"""

class Website:
    def __init__(self, name="", address="", description=""):
        self.name = name
        self.address = address
        self.description = description

    def input_data(self):
        self.name = input("Enter website name: ")
        self.address = input("Enter website address: ")
        self.description = input("Enter website description: ")

    def display_data(self):
        print("Website Name:", self.name)
        print("Website Address:", self.address)
        print("Website Description:", self.description)

    def update_description(self, new_description):
        self.description = new_description
        print("Website description updated.")

    def __str__(self):
        return f"Website: {self.name}, {self.address}, {self.description}"

    def __eq__(self, other):
        if isinstance(other, Website):
            return self.name == other.name and self.address == other.address
        return False

# main
website1 = Website("Codeium", "https://www.pinterest.com", "Ideas social network")
website2 = Website("Google", "https://www.google.com", "Internet search engine")

print(website1)
print(website2)
print(website1 == website2)
