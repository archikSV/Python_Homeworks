print("Task Date: 8.11.2023")
print("Task 3:\n")

"""
Створіть клас для конвертування з метричної системи в
англійську, та навпаки. Реалізуйте функціональність у вигляді
статичних методів. Обов’язково реалізуйте конвертування
заходів довжини. 
"""

class UnitConverter:
    @staticmethod
    def meters_to_feet(meters):
        return meters * 3.28084

    @staticmethod
    def feet_to_meters(feet):
        return feet / 3.28084

    @staticmethod
    def kilograms_to_pounds(kilograms):
        return kilograms * 2.20462

    @staticmethod
    def pounds_to_kilograms(pounds):
        return pounds / 2.20462

    @staticmethod
    def liters_to_gallons(liters):
        return liters * 0.264172

    @staticmethod
    def gallons_to_liters(gallons):
        return gallons / 0.264172

# main
meters = 10
feet = 32.8084
kilograms = 5
pounds = 11.0231
liters = 3.78541
gallons = 1

converted_feet = UnitConverter.meters_to_feet(meters)
converted_meters = UnitConverter.feet_to_meters(feet)
converted_pounds = UnitConverter.kilograms_to_pounds(kilograms)
converted_kilograms = UnitConverter.pounds_to_kilograms(pounds)
converted_gallons = UnitConverter.liters_to_gallons(liters)
converted_liters = UnitConverter.gallons_to_liters(gallons)

print(f"{meters} meters is equal to {converted_feet} feet.")
print(f"{feet} feet is equal to {converted_meters} meters.")
print(f"{kilograms} kilograms is equal to {converted_pounds} pounds.")
print(f"{pounds} pounds is equal to {converted_kilograms} kilograms.")
print(f"{liters} liters is equal to {converted_gallons} gallons.")
print(f"{gallons} gallons is equal to {converted_liters} liters.")