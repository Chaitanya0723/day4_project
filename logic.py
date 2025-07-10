def calculate_total_marks(marks):
    return sum(marks.values())


def calculate_percentage(total_marks, max_marks):
    return (total_marks / max_marks) * 100


def get_student_details(student):
    total_marks = calculate_total_marks(student["marks"])
    max_marks = 300
    percentage = calculate_percentage(total_marks, max_marks)

    return {
        "name": student["name"],
        "total_marks": total_marks,
        "percentage": percentage
    }


def add_student(students, id, name, marks):
    new_student = {
        "id": id,
        "name": name,
        "marks": marks
    }
    students.append(new_student)
