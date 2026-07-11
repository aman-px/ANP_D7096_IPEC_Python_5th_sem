def calculate(marks):
    total = sum(marks)
    return total

def percentage(marks):
	percentage = sum(marks)/5
	retrun percentage

name = input("Enter Name: ")

marks = []
print("Enter Marks:")
for i in range(5):
    m = int(input())
    marks.append(m)

total = calculate(marks)
percentage = percentage(marks)

if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

print("\nStudent Name :", name)
print("Marks :", marks)
print("Total :", total)
print("Percentage :", percentage)
print("Grade :", grade)