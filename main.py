print("Task Date: 9.10.2023")
print("Task 4:\n")

"""
Створіть множину english_vowels з голосними буквами
англійського алфавіту та множину spanish_vowels з
голосними буквами іспанського алфавіту. Знайдіть голосні,
які присутні і в англійській, і в іспанській мовах.
"""

english_vowels = {'a', 'e', 'i', 'o', 'u'}
spanish_vowels = {'a', 'e', 'i', 'o', 'u'}

common_vowels = english_vowels.intersection(spanish_vowels)
print(common_vowels)