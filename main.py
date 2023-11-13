print("Task Date: 18.10.2023")
print("Task 5:\n")

"""
Маємо текстовий файл. Підрахуйте кількість заданого
користувачем слова у ньому.
"""

def count_word_occurrences(file_path, word):
    count = 0
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        count += line.lower().count(word.lower())

    return count

# main
file_path = input("Enter the path to the file: ")
search_word = input("Enter the word to search for: ")
word_count = count_word_occurrences(file_path, search_word)
print(f"The word '{search_word}' occurs {word_count} times in the file.")