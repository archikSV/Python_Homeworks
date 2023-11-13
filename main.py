print("Task Date: 8.11.2023")
print("Task 1:\n")

"""
До вже реалізованого класу «Дріб» додайте статичний метод, який при виклику повертає кількість створених об’єктів
класу «Дріб».
"""

class Fraction:
    __num_objects = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.__num_objects += 1

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    @staticmethod
    def count_objects():
        return Fraction.__num_objects

# main
fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)
fraction3 = Fraction(5, 6)

print(fraction1)
print(fraction2)
print(fraction3)

print(Fraction.count_objects())  # prints 3
