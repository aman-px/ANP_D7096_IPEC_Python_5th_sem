print("Enter marks of 5 students with their names : ")

students = []
for i in range(5):
    name = input("Enter the name of student :")
    marks = float(input("Enter the marks of students :"))
    if marks > 100:
        exit("Marks should be less than or equal to 100 ")
    students.append({"name":name,"marks":marks})

print(students,"List Of Students")

for student in students:
    if student["marks"] > 75:
        print(student["name"],"eligible for admission : ")
