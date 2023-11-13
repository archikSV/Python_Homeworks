print("Task Date: 6.11.2023")
print("Task 2:\n")

"""
Створіть систему управління замовленнями
готелю. Кожне замовлення має містити інформацію
про клієнта, тип кімнати, кількість днів проживання та
вартість. Реалізуйте методи для додавання замовлення,
зміни типу кімнати та кількості днів, а також
видалення замовлення. Використайте інкапсуляцію для
захисту вартості від неправильних змін.
"""

class HotelOrder:
    def __init__(self, client, room_type, num_days, cost):
        self.client = client
        self.room_type = room_type
        self.num_days = num_days
        self.__cost = cost

    def get_cost(self):
        return self.__cost

    def set_room_type(self, new_room_type):
        self.room_type = new_room_type

    def set_num_days(self, new_num_days):
        self.num_days = new_num_days

    def delete_order(self):
        del self

    def calculate_cost(self):
        return self.num_days * self.__cost

    def __str__(self):
        return f"Client: {self.client}, Room Type: {self.room_type}, Number of Days: {self.num_days}, Cost: {self.__cost}"

# main
order1 = HotelOrder("John Doe", "Single Room", 5, 100.0)
order2 = HotelOrder("Jane Smith", "Double Room", 3, 150.0)

print(order1)
print(order2)
print(order1.client)
print(order2.room_type)

order1.set_room_type("Suite")
order2.set_num_days(7)

print(order1.room_type)
print(order2.num_days)

order1.delete_order()

# This will raise a NameError because order1 is deleted
print(order1)