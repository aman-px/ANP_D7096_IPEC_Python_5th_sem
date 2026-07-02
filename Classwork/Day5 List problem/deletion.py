print("Enter marks and names of 5 student:")
students = []
for i in range(5):
    name = input("Enter name of student : ")
    marks = float(input("Enter marks of student : "))
    if marks > 100:
        exit("Marks should be less than or equal to 100 ")
    students.append({"name":name,"marks":marks})

print(students,"List Of Students is :")

for i in range(len(students)-1,-1,-1):
    if students[i]["marks"] < 50:
        students.pop(i)
    
print("List of students after removing those who scored less than 50 marks : ",students)