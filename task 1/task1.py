students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    sid = int(input("Student ID: "))
    name = input("Student Name: ")
    aggregate = float(input("Aggregate Marks: "))

    subjects = []
    for j in range(3):
        marks = float(input("Enter subject marks: "))
        subjects.append(marks)

    attendance = float(input("Attendance Percentage: "))
    income = float(input("Annual Family Income: "))

    if (aggregate >= 75 and
        all(mark >= 60 for mark in subjects) and
        attendance >= 75 and income <= 250000):

        students.append({
            "id": sid,
            "name": name,
            "aggregate": aggregate,
            "subjects": subjects,
            "attendance": attendance
        })

    else:
        print(name, "- Not Eligible")

# Ranking eligible students
students.sort(key=lambda s: (
    -s["aggregate"],
    -s["attendance"],
    -sum(s["subjects"]),
    s["id"]
))

print("\n--- Scholarship Eligible Students ---")

for rank, s in enumerate(students, start=1):
    print("\nRank:", rank)
    print("ID:", s["id"])
    print("Name:", s["name"])
    print("Aggregate:", s["aggregate"])
    print("Attendance:", s["attendance"])
    print("Subject Total:", sum(s["subjects"]))

if len(students) == 0:
    print("No eligible students found.")
