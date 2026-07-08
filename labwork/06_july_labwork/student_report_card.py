# Nested dictionary to store student marks
students = {
    "Rahul": {"Math": 85, "Science": 90, "English": 88},
    "Priya": {"Math": 78, "Science": 95, "English": 82},
    "Ankit": {"Math": 91, "Science": 89, "English": 94}
}

# Dictionary to store total marks
total_marks = {}

# ------------------------------------
# 1. Calculate Total and Average Marks
# ------------------------------------
print("Total and Average Marks:\n")

for student, marks in students.items():

    total = sum(marks.values())
    average = total / len(marks)

    total_marks[student] = total

    print("Student:", student)
    print("Total:", total)
    print("Average:", average)
    print()

# ------------------------------------
# 2. Display the Topper
# ------------------------------------
topper = max(total_marks, key=total_marks.get)

print("Topper:")
print(topper, "with", total_marks[topper], "marks")

# ------------------------------------
# 3. Subject-wise Highest Marks
# ------------------------------------
subjects = ["Math", "Science", "English"]

print("\nSubject-wise Highest Marks:")

for subject in subjects:

    highest_marks = 0
    highest_student = ""

    for student, marks in students.items():

        if marks[subject] > highest_marks:
            highest_marks = marks[subject]
            highest_student = student

    print(subject, ":", highest_student, "-", highest_marks)

# ------------------------------------
# 4. Students with Average >= 85
# ------------------------------------
print("\nStudents with Average >= 85:")

for student, marks in students.items():

    average = sum(marks.values()) / len(marks)

    if average >= 85:
        print(student, ":", average)