class Student:
    def __init__(self):
        self.student_id = 0
        self.student_name = ""
        self.course = ""
        self.marks = 0
    
    def accept_data(self):
        self.student_id = input("Enter student id : ")
        self.student_name = input("Enter Student name : ")
        self.course = input("Enter course : ")
        self.marks = int(input("Enter marks : "))

    def check_result(self):
        if self.marks >= 35:
            return "Pass"
        else:
            return "Fail"
    
    def display_data(self):
        print("-----Student Details-----")
        print("Student ID : ",self.student_id)
        print("Name :",self.student_name)
        print("Course :",self.course)
        print("Marks :",self.marks)
        print("Result :",self.check_result())
# Creating Object Of Class Student : 
Student1 = Student()

# Calling All Methods : 
Student1.accept_data()
Student1.display_data()
