print("Task Date: 9.10.2023")
print("Task 5:\n")

"""
Напишіть функцію common_endings, яка приймає список
слів та повертає множину унікальних закінчень цих слів.
"""

def common_endings(words):
    endings = set()
    for word in words:
        for i in range(1, len(word)):
            endings.add(word[i:])
    return endings

# main
words = ["apple", "banana", "orange", "grapefruit"]
result = common_endings(words)
print(result)