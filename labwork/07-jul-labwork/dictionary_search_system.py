def search_student(student_dict, roll_no):
    """Search for a student by roll number in the dictionary."""
    return student_dict.get(str(roll_no), "Student Not Found")


# Main program
student_dict = {
    "101": "Aman",
    "102": "Riya",
    "103": "Kiran",
    "104": "Sara",
    "105": "Rahul"
}

roll_no = input("Enter roll number: ").strip()
result = search_student(student_dict, roll_no)
print("Student Name:", result)
