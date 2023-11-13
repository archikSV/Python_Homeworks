print("Task Date: 8.11.2023")
print("Task 2:\n")

"""
Створіть клас для конвертування температури з Цельсія
у Фаренгейт, і навпаки. У класі має знаходитися два статичні
методи: для конвертування з Цельсія у Фаренгейт і для конвертування з Фаренгейта у Цельсій. Також клас має розрахувати
кількість підрахунків температури та повернути це значення
статичним методом.
"""

class TemperatureConverter:
    __conversion_count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter.__conversion_count += 1
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter.__conversion_count += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def get_conversion_count():
        return TemperatureConverter.__conversion_count

# main
celsius = 25
fahrenheit = 77

converted_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
converted_celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)

print(f"{celsius} degrees Celsius is equal to {converted_fahrenheit} degrees Fahrenheit.")
print(f"{fahrenheit} degrees Fahrenheit is equal to {converted_celsius} degrees Celsius.")

print(TemperatureConverter.get_conversion_count())  # Prints the number of temperature conversions
