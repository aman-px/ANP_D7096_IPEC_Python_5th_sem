# Dictionary to store student names and their marks
students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Neha": 88,
    "Rohan": 95
}

# -----------------------------
# 1. Display all students and marks
# -----------------------------
print("Student Marks:")
for name, marks in students.items():
    print(name, ":", marks)

# -----------------------------
# 2. Add a new student
# -----------------------------
new_name = input("\nEnter new student name: ")
new_marks = int(input("Enter marks: "))

students[new_name] = new_marks

print("\nStudent added successfully!")

# -----------------------------
# 3. Update marks of an existing student
# -----------------------------
update_name = input("\nEnter student name to update marks: ")

if update_name in students:
    updated_marks = int(input("Enter new marks: "))
    students[update_name] = updated_marks
    print("Marks updated successfully!")
else:
    print("Student not found!")

# -----------------------------
# 4. Delete a student
# -----------------------------
delete_name = input("\nEnter student name to delete: ")

if delete_name in students:
    del students[delete_name]
    print("Student deleted successfully!")
else:
    print("Student not found!")

# -----------------------------
# 5. Display student with highest marks
# -----------------------------
highest_student = max(students, key=students.get)

print("\nStudent with Highest Marks:")
print(highest_student, ":", students[highest_student])

# -----------------------------
# Display final dictionary
# -----------------------------
print("\nFinal Student Records:")
for name, marks in students.items():
    print(name, ":", marks)