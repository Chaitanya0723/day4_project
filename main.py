from data import students
from logic import get_student_details, add_student


def display_student_report(students):
    for student in students:
        details = get_student_details(student)
        print(f"ID: {student['id']}")
        print(f"Name: {details['name']}")
        print(f"Total Marks: {details['total_marks']}")
        print(f"Percentage: {details['percentage']:.2f}%")
        print("-" * 30)


def add_new_student():
    id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    marks = {
        "math": int(input("Enter Math marks: ")),
        "science": int(input("Enter Science marks: ")),
        "english": int(input("Enter English marks: "))
    }

    add_student(students, id, name, marks)
    print(f"Student {name} added successfully!")


if __name__ == "__main__":
    while True:
        print("\n1. View Student Report")
        print("2. Add New Student")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            display_student_report(students)
        elif choice == "2":
            add_new_student()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
