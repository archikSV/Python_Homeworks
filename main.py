print("Task Date: 18.10.2023")
print("Task 2:\n")

"""
Маємо текстовий файл. Створіть новий файл і запишіть
до нього наступну статистику за вихідним файлом:
■ кількість символів;
■ кількість рядків;
■ кількість голосних літер;
■ кількість приголосних літер;
■ кількість цифр.
"""

def calculate_statistics(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

        # Calculate statistics
        num_characters = len(content)
        num_lines = content.count('\n')
        num_vowels = sum(content.lower().count(vowel) for vowel in 'aeiou')
        num_consonants = sum(content.lower().count(consonant) for consonant in 'bcdfghjklmnpqrstvwxyz')
        num_digits = sum(character.isdigit() for character in content)

    # Write statistics to output file
    with open(output_file, 'w') as file:
        file.write(f"Number of characters: {num_characters}\n")
        file.write(f"Number of lines: {num_lines}\n")
        file.write(f"Number of vowels: {num_vowels}\n")
        file.write(f"Number of consonants: {num_consonants}\n")
        file.write(f"Number of digits: {num_digits}\n")

# main
input_file = input("Enter the path to the input file: ")
output_file = input("Enter the path to the output file: ")

calculate_statistics(input_file, output_file)
