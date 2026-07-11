print("Enter marks of 6 students : ")
marks = []

for i in range(6):
    mark = float(input("Enter the marks of student : "))
    if mark > 100 or mark < 0:
        exit("Marks should be less than 100 and should be positive :")
    marks.append(mark)
    
print("List before performing bonus marks : ",marks)
for i in range(6):
    if marks[i] > 40 and marks[i] < 96:
        marks[i] = marks[i] + 5
print("List after performing bonus marks : ",marks)
marks.sort()
print("List after sorting : ",marks)
marks.reverse()
print("List after reversing to get descending order : ",marks)
min_value = min((marks))
print("Lowest mark of the student is : ",min_value)
i = marks.index(min_value)
print("Index of lowest mark : ", i)
marks.pop(i)
print("List after removing the lowest mark and the final List is : ",marks)





