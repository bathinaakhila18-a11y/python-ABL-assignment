# Examination Result and Grace-Mark Validation

print("===== EXAMINATION RESULT SYSTEM =====")

student_name = input("Enter student name: ")

subjects = ["Python", "Mathematics", "English",
            "Physics", "Chemistry"]

pass_marks = 40
maximum_marks = 100
maximum_grace = 5

total = 0
grace_used = 0
all_pass = True

for subject in subjects:

    marks = int(input("Enter marks in " + subject + ": "))

    # Validate marks
    if marks < 0 or marks > maximum_marks:
        print("Invalid Marks! Enter marks between 0 and 100.")
        break

    grace = 0

    # Apply grace marks
    if marks < pass_marks:

        if marks >= pass_marks - maximum_grace:
            grace = pass_marks - marks
            marks = min(marks + grace, maximum_marks)

        else:
            all_pass = False

    if marks < pass_marks:
        all_pass = False

    total += marks
    grace_used += grace

    print("Subject:", subject)
    print("Final Marks:", marks)
    print("Grace Marks:", grace)

else:
    # Calculate percentage
    percentage = total / (len(subjects) * maximum_marks) * 100

    # Result classification
    if not all_pass:
        result = "FAIL"

    elif percentage >= 75:
        result = "DISTINCTION"

    elif percentage >= 60:
        result = "FIRST CLASS"

    elif percentage >= 50:
        result = "SECOND CLASS"

    else:
        result = "PASS"

    # Display final result
    print("\n===== FINAL RESULT =====")
    print("Student Name:", student_name)
    print("Total Marks:", total, "/", len(subjects) * 100)
    print("Percentage:", round(percentage, 2), "%")
    print("Total Grace Marks:", grace_used)
    print("Final Result:", result)
