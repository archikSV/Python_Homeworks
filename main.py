print("Task Date: 1.11.2023")
print("Task 4:\n")

"""
Реалізуйте клас «Годинник». Збережіть у класі:
назву моделі годинника, виробника годинника, рік
випуску, ціну годинника, тип годинника (наручний,
настінний і т. д.). Реалізуйте конструктор та методи
класу для введення-виведення даних, а також для
інших операцій. Використовуйте механізм
перевантаження методів.

"""

class Watch:
    def __init__(self, model="", manufacturer="", year=0, price=0, watch_type=""):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.price = price
        self.watch_type = watch_type

    def input_data(self):
        self.model = input("Enter watch model: ")
        self.manufacturer = input("Enter watch manufacturer: ")
        self.year = int(input("Enter year of manufacture: "))
        self.price = float(input("Enter watch price: "))
        self.watch_type = input("Enter watch type: ")

    def display_data(self):
        print("Watch Model:", self.model)
        print("Watch Manufacturer:", self.manufacturer)
        print("Year of Manufacture:", self.year)
        print("Watch Price:", self.price)
        print("Watch Type:", self.watch_type)

    def update_price(self, new_price):
        self.price = new_price
        print("Watch price updated.")

    def __str__(self):
        return f"Watch: {self.model}, {self.manufacturer}, {self.year}, {self.price}, {self.watch_type}"

    def __eq__(self, other):
        if isinstance(other, Watch):
            return self.model == other.model and self.manufacturer == other.manufacturer
        return False

# main
watch1 = Watch("G-Shock", "Casio", 2020, 200.0, "Wristwatch")
watch2 = Watch("Submariner", "Rolex", 2019, 10000.0, "Wristwatch")

print(watch1)
print(watch2)
print(watch1 == watch2)
