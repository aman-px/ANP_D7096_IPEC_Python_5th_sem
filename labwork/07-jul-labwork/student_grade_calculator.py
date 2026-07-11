# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

# Main program
for i in range(1, 6):
    marks = float(input(f"Enter marks of Student {i} (0-100): "))
    while marks < 0 or marks > 100:
        print("Please enter marks between 0 and 100.")
        marks = float(input(f"Enter marks of Student {i} (0-100): "))
    grade = calculate_grade(marks)
    print(f"Student {i}: Marks = {marks}, Grade = {grade}")