print("Task Date: 1.11.2023")
print("Task 2:\n")

"""
До вже реалізованого класу «Місто» додайте конструктор та необхідні перевантажені методи.
"""

class City:
    def __init__(self, city_name="", region_name="", country_name="", population=0, postal_code="", phone_code=""):
        self.city_name = city_name
        self.region_name = region_name
        self.country_name = country_name
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def input_data(self):
        self.city_name = input("Enter city name: ")
        self.region_name = input("Enter region name: ")
        self.country_name = input("Enter country name: ")
        self.population = int(input("Enter population: "))
        self.postal_code = input("Enter postal code: ")
        self.phone_code = input("Enter phone code: ")

    def display_data(self):
        print("City Name:", self.city_name)
        print("Region Name:", self.region_name)
        print("Country Name:", self.country_name)
        print("Population:", self.population)
        print("Postal Code:", self.postal_code)
        print("Phone Code:", self.phone_code)

    def update_population(self, new_population):
        self.population = new_population
        print("Population updated.")

    def __str__(self):
        return f"City: {self.city_name}, {self.region_name}, {self.country_name}, {self.population}, {self.postal_code}, {self.phone_code}"

    def __eq__(self, other):
        if isinstance(other, City):
            return self.city_name == other.city_name and self.country_name == other.country_name
        return False

# main
city1 = City("New York", "New York", "USA", 8500000, "10001", "+1")
city2 = City("Los Angeles", "California", "USA", 4000000, "90001", "+1")

print(city1)
print(city2)
print(city1 == city2)
