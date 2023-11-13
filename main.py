print("Task Date: 18.10.2023")
print("Task 4:\n")

"""
Маємо текстовий файл. Знайдіть довжину найдовшого
рядка.
"""

def find_longest_line_length(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    max_length = 0
    for line in lines:
        line_length = len(line.strip())
        if line_length > max_length:
            max_length = line_length

    return max_length

# main
file_path = input("Enter the path to the file: ")
longest_line_length = find_longest_line_length(file_path)
print(f"The length of the longest line is: {longest_line_length}")
