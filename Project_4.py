
Students = {
    101: {"name": "Saurabh Pandey", "Marks": [98, 89, 87]},
    102: {"name": "Abhayjeet Kumar", "Marks": [99, 99, 97]},
    103: {"name": "Anshu Kumar Singh", "Marks": [94, 99, 98]},
    104: {"name": "Chandan Kumar", "Marks": [95, 99, 88]},
    105: {"name": "Naval Kishor", "Marks": [99, 99, 99]}
}

def validate_student_record(student_id, name, marks):
    if not isinstance(name, str) or not name.strip():
        return None

    if not isinstance(marks, list) or len(marks) == 0:
        return None

    for mark in marks:
        if (not isinstance(mark, (int, float))
                or isinstance(mark, bool)
                or mark < 0 or mark > 100):
            return None

    return {
        "name": name,
        "Marks": marks
    }


def add_student(student_id, name, marks):
    if student_id in Students:
        print("Student ID already exists.")
        return

    record = validate_student_record(student_id, name, marks)

    if record is None:
        print("Invalid student record.")
    else:
        Students[student_id] = record
        print("Student added successfully.")


def get_total(Student_id):
    return sum(Students[Student_id]["Marks"])


def avg_marks(Student_id):
    marks = Students[Student_id]["Marks"]
    return sum(marks) / len(marks)


def get_grade(avg):
    if avg >= 75:
        return "Distinction"
    elif avg >= 60:
        return "First Division"
    elif avg >= 40:
        return "Pass"
    else:
        return "Fail"


def build_report(student, show_marks=True):
    marks = student["Marks"]
    total = sum(marks)
    average = total / len(marks)
    grade = get_grade(average)
    report = ""

    if show_marks:
        report += f"Marks: {marks}\n"

    report += f"Total: {total}\n"
    report += f"Average: {average:.2f}\n"
    report += f"Grade: {grade}\n"

    return report


print("\n STUDENT PERFORMANCE REPORT \n")
print(f"{'Roll No.':<10}{'Student Name':<23}{'Total':<10}{'Average':<12}{'Grade'}")

for roll in Students:
    total = get_total(roll)
    average = avg_marks(roll)
    grade = get_grade(avg=average)

    print(f"{roll:<10}{Students[roll]['name']:<23}{total:<10}{average:<12.2f}{grade}")


def get_top_students(records):
    top_students = filter(
        lambda student: avg_marks(student) >= 75,
        records
    )
    return list(top_students)


top_students = get_top_students(Students)

print("\nHIGH PERFORMING STUDENTS")

for roll in top_students:
    print(Students[roll]["name"], "-", avg_marks(roll))


student_names = list(
    map(lambda roll: Students[roll]["name"], Students)
)

print("\nALL STUDENT NAMES")
print(student_names)


def calculate_any_average(*marks):

    if len(marks) == 0:
        return 0

    total = sum(marks)
    average = total / len(marks)
    return average


print("\nAverage of supplied marks:",
      calculate_any_average(90, 85, 95, 80))


def class_summary(**options):

    title = options.get("title", "Class Report")
    passing_mark = options.get("passing_mark", 40)

    print("\n", title)

    passed = 0

    for roll in Students:
        if avg_marks(roll) >= passing_mark:
            passed += 1

    print("Total Students:", len(Students))
    print("Students Passed:", passed)
    print("Students Failed:", len(Students) - passed)


class_summary(title="Student Class Summary", passing_mark=40)


def class_average():

    total = 0

    for roll in Students:
        total += avg_marks(roll)

    return total / len(Students)


print("\nClass Average:", format(class_average(), ".2f"))


def recursive_sum(n):

    if n == 0:
        return 0
    elif n < 0:
        return None
    else:
        return n + recursive_sum(n - 1)


print("\nRECURSION")
print("Sum from 1 to 5:", recursive_sum(5))
print("Sum from 1 to 7:", recursive_sum(7))
print("Sum from 1 to 10:", recursive_sum(10))


def scope_example():
    message = "This is a local variable."
    print("\n", message)


scope_example()


print("\n INDIVIDUAL STUDENT REPORTS ")

for roll in Students:

    print("\nRoll Number:", roll)
    print("Student Name:", Students[roll]["name"])
    print(build_report(Students[roll]))
