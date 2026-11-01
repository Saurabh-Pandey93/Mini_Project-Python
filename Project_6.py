
import json
import csv
import os
import datetime as dt

JSON_FILE = "students.json"
CSV_FILE = "students.csv"
LOG_FILE = "activity_log.txt"

SUBJECTS = ["Python", "Maths", "DBMS"]

def load_students():
    if os.path.exists(JSON_FILE):
        try:
            with open(JSON_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: JSON file contains invalid data.")
            return None

    return {}

def save_students(students):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)

def log_activity(message):
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as file:
            file.writelines(["STUDENT RECORDS ACTIVITY LOG\n",
                             "-----------------------------\n"])

    timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"{timestamp} - {message}\n")


def get_marks():
    marks = {}
    for subject in SUBJECTS:
        while True:
            try:
                value = float(input(f"Enter {subject} marks: "))
                if 0 <= value <= 100:
                    marks[subject] = value
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
    return marks

def add_student(students):
    print("\n ADD STUDENT")
    student_id = input("Enter Student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return
    if student_id in students:
        print("Student ID already exists!")
        return
    name = input("Enter Name: ").strip()
    department = input("Enter Department: ").strip()
    if not name or not department:
        print("Name and department are required.")
        return
    marks = get_marks()

    students[student_id] = {
        "name": name,
        "department": department,
        "marks": marks
    }

    save_students(students)
    log_activity(f"Added student {student_id}")
    print("Student record saved successfully!")

def display_students(students):
    print("\n--- ALL STUDENT RECORDS ---")

    if not students:
        print("No student records found.")
        return

    for student_id, details in students.items():
        print("-" * 40)
        print("Student ID :", student_id)
        print("Name       :", details["name"])
        print("Department :", details["department"])

        for subject, mark in details["marks"].items():
            print(f"{subject:<12}: {mark:g}")

def search_student(students):
    student_id = input("\nEnter Student ID to search: ").strip()

    if student_id in students:
        details = students[student_id]

        print("\n STUDENT FOUND ")
        print("ID         :", student_id)
        print("Name       :", details["name"])
        print("Department :", details["department"])
        print("Marks      :", details["marks"])
    else:
        print("Student not found.")

def update_student(students):
    student_id = input("\nEnter Student ID: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    print("Enter updated marks:")
    students[student_id]["marks"] = get_marks()

    save_students(students)
    log_activity(f"Updated student {student_id}")

    print("Student record updated successfully!")

def export_csv(students):
    if not students:
        print("No records available to export.")
        return

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Student ID", "Name", "Department",
            "Python", "Maths", "DBMS"
        ])

        for student_id, details in students.items():
            marks = details["marks"]

            writer.writerow([
                student_id,
                details["name"],
                details["department"],
                marks["Python"],
                marks["Maths"],
                marks["DBMS"]
            ])

    log_activity("Exported student records to CSV")
    print(f"CSV export completed: {CSV_FILE}")

def json_demo(students):
    student_id = input("\nEnter Student ID: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    json_string = json.dumps(students[student_id], indent=4)

    print("\nJSON String:")
    print(json_string)

    python_data = json.loads(json_string)

    print("\nConverted back to Python dictionary:")
    print(python_data)

def view_log():
    if not os.path.exists(LOG_FILE):
        print("No activity log found.")
        return

    print("\n1. Read entire file")
    print("2. Read first line")
    print("3. Read all lines")

    choice = input("Enter choice: ").strip()

    with open(LOG_FILE, "r", encoding="utf-8") as file:

        if choice == "1":
            print(file.read())

        elif choice == "2":
            print(file.readline())

        elif choice == "3":
            lines = file.readlines()
            for line in lines:
                print(line, end="")

        else:
            print("Invalid choice.")
def main():
    students = load_students()

    if students is None:
        print("Program stopped. Please fix the JSON file first.")
        return

    print("=" * 45)
    print("       STUDENT RECORDS MANAGEMENT")
    print("=" * 45)

    while True:
        print("\n1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Export Records to CSV")
        print("6. View Activity Log")
        print("7. JSON String Demo")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            export_csv(students)

        elif choice == "6":
            view_log()

        elif choice == "7":
            json_demo(students)

        elif choice == "8":
            print("Thank you for using Student Records Management!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
