print("Task Date: 27.09.2023")
print("Task 3:\n")

"""
Реалізуйте декоратор, який кешує результати в
список вже викликаних функцій та повертає збережений
результат при наступних викликах з тими ж аргументами.
"""

def cache_results(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper

# main
@cache_results
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# First call
print(fibonacci(5))

# Second call with the same argument
print(fibonacci(5))

# Another call with a different argument
print(fibonacci(6))
