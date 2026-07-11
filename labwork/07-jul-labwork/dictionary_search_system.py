def search_student(student_dict, roll_no):
    if roll_no in student_dict:
        return student_dict[roll_no]
    else:
        return "Student not found"



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
