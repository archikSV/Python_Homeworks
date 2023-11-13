print("Task Date: 4.10.2023")
print("Task 2:\n")

"""
Напишіть програму «Книги». Створіть два списки з даними. Один список зберігає назви книг, другий — роки випуску.
Реалізуйте меню для користувача:
■ відсортувати за назвою книг;
■ відсортувати за рокам випуску;
■ вивести список книг з назвами та роками випуску;
■ вихід.
"""

def sort_by_book_title(book_titles, release_years):
    sorted_data = sorted(zip(book_titles, release_years))
    sorted_book_titles, sorted_release_years = zip(*sorted_data)
    return sorted_book_titles, sorted_release_years

def sort_by_release_year(book_titles, release_years):
    sorted_data = sorted(zip(release_years, book_titles))
    sorted_release_years, sorted_book_titles = zip(*sorted_data)
    return sorted_release_years, sorted_book_titles

def print_books(book_titles, release_years):
    for book_title, release_year in zip(book_titles, release_years):
        print(f"Book: {book_title} \t Release Year: {release_year}")

# Sample data
book_titles = ["Book A", "Book C", "Book B", "Book D"]
release_years = [2005, 2010, 2000, 2015]

# Main program loop
while True:
    print("Menu:")
    print("1. Sort by Book Title")
    print("2. Sort by Release Year")
    print("3. Print Books")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        sorted_book_titles, sorted_release_years = sort_by_book_title(book_titles, release_years)
        print_books(sorted_book_titles, sorted_release_years)
    elif choice == "2":
        sorted_release_years, sorted_book_titles = sort_by_release_year(book_titles, release_years)
        print_books(sorted_book_titles, sorted_release_years)
    elif choice == "3":
        print_books(book_titles, release_years)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")