# logic.py

def calculate_total_marks(marks):
    """
    Calculate the total marks obtained by the student.
    marks: dictionary with subject names as keys and marks as values.
    Returns the total marks.
    """
    return sum(marks.values())


def calculate_percentage(total_marks, max_marks):
    """
    Calculate the percentage based on total marks and maximum possible marks.
    total_marks: the sum of marks obtained by the student.
    max_marks: the total possible marks across all subjects.
    Returns the percentage.
    """
    return (total_marks / max_marks) * 100


def get_student_details(student):
    """
    Get the total marks and percentage for a given student.
    student: a dictionary containing student's data.
    Returns a dictionary with total marks and percentage.
    """
    total_marks = calculate_total_marks(student["marks"])
    max_marks = 300  # Assuming 3 subjects with max marks as 100 each
    percentage = calculate_percentage(total_marks, max_marks)

    return {
        "name": student["name"],
        "total_marks": total_marks,
        "percentage": percentage
    }


def add_student(students, id, name, marks):
    """
    Adds a new student to the students list.
    students: list of students.
    id: student ID.
    name: student's name.
    marks: dictionary with subject names as keys and marks as values.
    """
    new_student = {
        "id": id,
        "name": name,
        "marks": marks
    }
    students.append(new_student)
