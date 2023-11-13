print("Task Date: 18.10.2023")
print("Task 1:\n")

"""
Маємо два текстові файли. З’ясуйте, чи співпадають їхні
рядки. Якщо ні, то виведіть із кожного файлу рядок, який не
співпадає.
"""

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        for line1, line2 in zip(lines1, lines2):
            line1 = line1.strip()
            line2 = line2.strip()
            if line1 != line2:
                print(f"File 1: {line1}")
                print(f"File 2: {line2}")
                print()

# main
file1 = input("Enter the path to the first file: ")
file2 = input("Enter the path to the second file: ")

compare_files(file1, file2)
