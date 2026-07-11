students = {}
#write a python program to manage student records.
def add():
    roll = input("Roll No: ")
    name = input("Name: ")
    marks = input("Marks: ")
    students[roll] = {"Name": name, "Marks": marks}
    print("Student Added Successfully")

def search():
    roll = input("Enter Roll No: ")
    if roll in students:
        print("Roll No:", roll)
        print("Name:", students[roll]["Name"])
        print("Marks:", students[roll]["Marks"])
    else:
        print("Record Not Found")

def display():
    for roll in students:
        print(roll, students[roll]["Name"], students[roll]["Marks"])

while True:
    print("\n1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        add()
    elif ch == 2:
        search()
    elif ch == 3:
        display()
    elif ch == 4:
        print("Thank You")
        break
    else:
        print("Invalid Choice")