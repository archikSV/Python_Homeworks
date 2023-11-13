print("Task Date: 6.11.2023")
print("Task 1:\n")

"""
Створіть систему управління замовленнями
готелю. Кожне замовлення має містити інформацію
про клієнта, тип кімнати, кількість днів проживання та
вартість. Реалізуйте методи для додавання замовлення,
зміни типу кімнати та кількості днів, а також
видалення замовлення. Використайте інкапсуляцію для
захисту вартості від неправильних змін.
"""

# main
class HotelOrder:
    def __init__(self, client="", room_type="", num_days=0, cost=0):
        self.__client = client
        self.__room_type = room_type
        self.__num_days = num_days
        self.__cost = cost

    def get_client(self):
        return self.__client

    def get_room_type(self):
        return self.__room_type

    def get_num_days(self):
        return self.__num_days

    def set_room_type(self, new_room_type):
        self.__room_type = new_room_type

    def set_num_days(self, new_num_days):
        self.__num_days = new_num_days

    def delete_order(self):
        del self

    def calculate_cost(self):
        return self.__num_days * self.__cost

    def __str__(self):
        return f"Client: {self.__client}, Room Type: {self.__room_type}, Number of Days: {self.__num_days}, Cost: {self.__cost}"

# main
order1 = HotelOrder("John Doe", "Single Room", 5, 100.0)
order2 = HotelOrder("Jane Smith", "Double Room", 3, 150.0)

print(order1)
print(order2)
print(order1.get_client())
print(order2.get_room_type())

order1.set_room_type("Suite")
order2.set_num_days(7)

print(order1.get_room_type())
print(order2.get_num_days())

order1.delete_order()

# This will raise an AttributeError because order1 is deleted
print(order1)