
# Integrated Student Record Consistency Checker

students = [
    ("101", "Ravi", 85, 90, "Python"),
    ("102", "Kiran", 75, 80, "Java"),
    ("101", "Sita", 90, 95, "Python"),
    ("104", "", 110, 60, "C"),
    ("105", "Arun", 65, 70, ""),
    ("106", "Priya", 88, 85, "Python")
]

valid_records = []
invalid_records = []
used_ids = set()

for student in students:

    sid, name, marks, attendance, course = student
    errors = []

    # Check missing values
    if any(value is None or value == ""
           for value in student):
        errors.append("Missing value")

    # Check duplicate ID
    if sid is not None and sid != "":
        if sid in used_ids:
            errors.append("Duplicate student ID")
        else:
            used_ids.add(sid)

    # Validate marks
    if not isinstance(marks, (int, float)) or isinstance(marks, bool):
        errors.append("Invalid marks")
    elif marks < 0 or marks > 100:
        errors.append("Marks out of range")

    # Validate attendance
    if not isinstance(attendance, (int, float)) or isinstance(attendance, bool):
        errors.append("Invalid attendance")
    elif attendance < 0 or attendance > 100:
        errors.append("Attendance out of range")
    elif attendance < 75:
        errors.append("Low attendance")

    # Validate name
    if not isinstance(name, str) or not name.strip():
        errors.append("Invalid student name")

    # Validate course
    if not isinstance(course, str) or not course.strip():
        errors.append("Invalid course")

    # Classify records
    if len(errors) == 0:
        valid_records.append(student)
    else:
        invalid_records.append((student, errors))


# Display valid records
print("\n----- VALID STUDENT RECORDS -----")

for record in valid_records:
    print(record)


# Display invalid records
print("\n----- INVALID STUDENT RECORDS -----")

for record, errors in invalid_records:
    print("\nRecord:", record)
    for error in errors:
        print("Error:", error)


# Final report
print("\n----- FINAL REPORT -----")
print("Total Students:", len(students))
print("Valid Records:", len(valid_records))
print("Invalid Records:", len(invalid_records))
print("Duplicate IDs:", len(students) - len(used_ids))

