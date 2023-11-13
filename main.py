print("Task Date: 18.10.2023")
print("Task 6:\n")

"""
Маємо текстовий файл. Знайдіть і замініть у ньому задане
слово. Яке слово шукати і на яке замінювати — встановлюється користувачем.
"""

def replace_word(file_path, search_word, replacement_word):
    with open(file_path, 'r') as file:
        content = file.read()

    # Perform the replacement
    updated_content = content.replace(search_word, replacement_word)

    # Write the updated content to the file
    with open(file_path, 'w') as file:
        file.write(updated_content)

# main
file_path = input("Enter the path to the file: ")
search_word = input("Enter the word to search for: ")
replacement_word = input("Enter the word to replace it with: ")
replace_word(file_path, search_word, replacement_word)
print("Word replacement completed.")