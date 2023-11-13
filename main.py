print("Task Date: 30.10.2023")
print("Task 3:\n")

"""
Створіть клас «Країна». Збережіть у класі: назву країни,
назву континенту, кількість жителів країни, телефонний
код країни, назву столиці, назву міст країни. Реалізуйте
методи класу для введення-виведення даних та інших
операцій.

"""

class Country:
    def __init__(self):
        self.country_name = ""
        self.continent_name = ""
        self.population = 0
        self.phone_code = ""
        self.capital_name = ""
        self.city_names = []

    def input_data(self):
        self.country_name = input("Enter country name: ")
        self.continent_name = input("Enter continent name: ")
        self.population = int(input("Enter population: "))
        self.phone_code = input("Enter phone code: ")
        self.capital_name = input("Enter capital name: ")
        self.city_names = input("Enter city names (comma-separated): ").split(",")

    def display_data(self):
        print("Country Name:", self.country_name)
        print("Continent Name:", self.continent_name)
        print("Population:", self.population)
        print("Phone Code:", self.phone_code)
        print("Capital Name:", self.capital_name)
        print("City Names:", ", ".join(self.city_names))

    def add_city(self, city_name):
        self.city_names.append(city_name)
        print("City added.")

# Main
country = Country()
country.input_data()
print("---")
country.display_data()
print("---")
new_city = input("Enter new city name: ")
country.add_city(new_city)
print("---")
country.display_data()
