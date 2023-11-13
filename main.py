print("Task Date: 18.10.2023")
print("Task 3:\n")

"""
Маємо текстовий файл. Видаліть з нього останній рядок.
Результат запишіть до іншого файлу.
"""

def remove_last_line(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Remove last line
    lines = lines[:-1]

    # Write remaining lines to output file
    with open(output_file, 'w') as file:
        file.writelines(lines)

# main
input_file = input("Enter the path to the input file: ")
output_file = input("Enter the path to the output file: ")

remove_last_line(input_file, output_file)
