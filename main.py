print("Task Date: 27.09.2023")
print("Task 1:\n")

"""
Реалізуйте замикання, яке дозволяє вводити та
видаляти елементи зі списку. Замикання повинно мати дві
функції: add_element та remove_element. Перша додає
елемент до списку, а друга видаляє його.
"""

def closure():
    elements = []

    def add_element(element):
        elements.append(element)
        print("Element added:", element)

    def remove_element(element):
        if element in elements:
            elements.remove(element)
            print("Element removed:", element)
        else:
            print("Element not found in the list")

    return add_element, remove_element

# Create an instance of the closure
add_func, remove_func = closure()

# Add elements
add_func(5)
add_func(8)
add_func(2)

# Remove an element
remove_func(8)

# Try to remove a non-existent element
remove_func(10)