print("Task Date: 11.10.2023")
print("Task 2:\n")

"""
Створіть програму «Англо-французький словник». Збережіть слово англійською та його переклад на французьку.
Реалізуйте можливість додавати, видаляти, знаходити та
змінювати дані. Використовуйте словник для збереження
інформації.
"""

dictionary = {}

def add_word(word, translation):
    dictionary[word] = translation

def delete_word(word):
    if word in dictionary:
        del dictionary[word]
    else:
        print(f"The word '{word}' is not in the dictionary.")

def search_word(word):
    if word in dictionary:
        return dictionary[word]
    else:
        return f"The word '{word}' is not in the dictionary."

def update_word(word, translation):
    if word in dictionary:
        dictionary[word] = translation
    else:
        print(f"The word '{word}' is not in the dictionary.")

# main
add_word("apple", "pomme")
add_word("cat", "chat")
add_word("dog", "chien")

print(search_word("apple"))  # pomme

update_word("apple", "pomme fruit")
print(search_word("apple"))  # pomme fruit

delete_word("cat")
print(search_word("cat"))  # The word 'cat' is not in the dictionary.
