
# Student Performance Trend Analysis

print("===== STUDENT PERFORMANCE ANALYSIS =====")

name = input("Enter student name: ")

subjects = ["Python", "Maths", "English",
            "Physics", "Chemistry"]

exam1 = []
exam2 = []
exam3 = []

# Enter examination marks
valid = True

for subject in subjects:

    print("\nEnter marks for", subject)

    m1 = int(input("Exam 1: "))
    m2 = int(input("Exam 2: "))
    m3 = int(input("Exam 3: "))

    # Validate marks
    if not (0 <= m1 <= 100 and
            0 <= m2 <= 100 and
            0 <= m3 <= 100):

        print("Invalid Marks! Enter marks between 0 and 100.")
        valid = False
        break

    exam1.append(m1)
    exam2.append(m2)
    exam3.append(m3)

if valid:

    total = 0
    weak_subjects = []

    print("\n===== PERFORMANCE TRENDS =====")

    for i in range(len(subjects)):

        change = exam3[i] - exam2[i]

        print("\nSubject:", subjects[i])

        if change > 0:
            print("Improvement:", change, "marks")

        elif change < 0:
            print("Decline:", abs(change), "marks")

        else:
            print("No Change")

        # Identify consistently weak subjects
        if (exam1[i] < 40 and
            exam2[i] < 40 and
            exam3[i] < 40):

            weak_subjects.append(subjects[i])

        total += exam3[i]

    # Calculate percentage
    percentage = total / 500 * 100

    # Classify student
    if any(mark < 40 for mark in exam3):
        result = "FAIL"

    elif percentage >= 75:
        result = "DISTINCTION"

    elif percentage >= 60:
        result = "FIRST CLASS"

    elif percentage >= 50:
        result = "SECOND CLASS"

    else:
        result = "PASS"

    # Display final report
    print("\n===== FINAL PERFORMANCE REPORT =====")

    print("Student Name:", name)
    print("Latest Exam Total:", total, "/ 500")
    print("Percentage:", round(percentage, 2), "%")

    if weak_subjects:
        print("Weak Subjects:", weak_subjects)
    else:
        print("Weak Subjects: None")

    print("Final Classification:", result)
