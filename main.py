print("Task Date: 2.10.2023")
print("Task 2:\n")

"""
Написати програму «Успішність». Користувач вводить
10 оцінок студента. Оцінки від 1 до 12. Реалізуйте меню для
користувача:
■ виведення оцінок (виведення вмісту списку);
■ перескладання іспиту (користувач вводить номер елемента
списку та нову оцінку);
■ отримання стипендії (стипендію отримують, якщо середній бал не нижче 10.7);
■ виведення відсортованого списку оцінок: за зростанням
або спаданням.
"""


def display_grades(grades):
    print("Student's grades:", grades)


def rearrange_exam(grades):
    index = int(input("Enter the index of the grade to rearrange: "))
    new_grade = int(input("Enter the new grade: "))
    grades[index - 1] = new_grade
    print("Grades after rearranging the exam:", grades)


def get_scholarship(grades):
    average = sum(grades) / len(grades)
    if average >= 10.7:
        print("The student is eligible for a scholarship")
    else:
        print("The student is not eligible for a scholarship")


def sort_grades(grades):
    sort_order = input("Enter 'asc' to sort in ascending order or 'desc' to sort in descending order: ")
    if sort_order == "asc":
        sorted_grades = sorted(grades)
    elif sort_order == "desc":
        sorted_grades = sorted(grades, reverse=True)
    else:
        print("Invalid input")
        return
    print("Sorted grades:", sorted_grades)


# Main function
def main():
    grades = []
    for _ in range(10):
        grade = int(input("Enter the student's grade (1 to 12): "))
        grades.append(grade)

    while True:
        print("\nMenu:")
        print("1. Display grades")
        print("2. Rearrange exam")
        print("3. Get scholarship")
        print("4. Sort grades")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            display_grades(grades)
        elif choice == "2":
            rearrange_exam(grades)
        elif choice == "3":
            get_scholarship(grades)
        elif choice == "4":
            sort_grades(grades)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid input")


# main
main()