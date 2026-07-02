print("Enter the marks of 5 students :")
marks = []

for i in range(5):
    mark = float(input("Enter the marks of student : "))
    if mark < 0 or mark > 100:
        exit("Marks should be less than or equal to 100 and should be positive :")
    marks.append(mark)

print("List is : ",marks)

mark1 = float(input("Enter the marks of 1st transfer student : "))
mark2 = float(input("Enter the mark of 2nd ttransfer student : "))
if (mark1 < 0 or mark1 > 100) and (mark2 < 0 or mark2 > 100):
    exit("Marks should be less than or equal to 100 and should be positive :")
marks.append(mark1)
marks.append(mark2)
print("List after appending marks of 2 transfer students : ",marks)
marks[0] = 75
print("List after changing the marks of 1st student to 75 : ",marks)
marks.sort()
print("List after sorting : ",marks)
marks.reverse()
print("List after reversing to get descending order : ",marks)
marks.pop(6)
print("List after removing lowest mark and the final List is : ",marks)



