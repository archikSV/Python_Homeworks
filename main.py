print("Task Date: 30.10.2023")
print("Task 2:\n")

"""
Створіть клас «Місто». Збережіть у класі: назву міста,
назву регіону, назву країни, кількість жителів у місті,
поштовий індекс міста, телефонний код міста. Реалізуйте
методи класу для введення-виведення даних та інших
операцій.
"""

class City:
    def __init__(self):
        self.city_name = ""
        self.region_name = ""
        self.country_name = ""
        self.population = 0
        self.postal_code = ""
        self.phone_code = ""

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

# main
city = City()
city.input_data()
print("---")
city.display_data()
print("---")
new_population = int(input("Enter new population: "))
city.update_population(new_population)
print("---")
city.display_data()
