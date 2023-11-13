print("Task Date: 1.11.2023")
print("Task 3:\n")

"""
До вже реалізованого класу «Країна» додайте конструктор та необхідні перевантажені методи.
"""

class Country:
    def __init__(self, country_name="", continent_name="", population=0, phone_code="", capital_name="", city_names=[]):
        self.country_name = country_name
        self.continent_name = continent_name
        self.population = population
        self.phone_code = phone_code
        self.capital_name = capital_name
        self.city_names = city_names

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

    def __str__(self):
        return f"Country: {self.country_name}, {self.continent_name}, {self.population}, {self.phone_code}, {self.capital_name}, {self.city_names}"

    def __eq__(self, other):
        if isinstance(other, Country):
            return self.country_name == other.country_name and self.continent_name == other.continent_name
        return False

# main
country1 = Country("USA", "North America", 328200000, "+1", "Washington, D.C.", ["New York", "Los Angeles", "Chicago"])
country2 = Country("Canada", "North America", 37590000, "+1", "Ottawa", ["Toronto", "Montreal", "Vancouver"])

print(country1)
print(country2)
print(country1 == country2)
