# Student Result Analyzer Program

# Step 1: Accept number of students
n = int(input("Enter number of students: "))

# Step 2: Create an empty list to store marks
marks = []

# Step 3: Accept marks of each student
for i in range(n):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

# Step 4: Calculate highest and lowest marks
highest_marks = max(marks)
lowest_marks = min(marks)

# Step 5: Calculate average marks
average_marks = sum(marks) / n

# Step 6: Count passed and distinction students
pass_count = 0
distinction_count = 0

for m in marks:
    if m >= 40:
        pass_count += 1
    if m >= 75:
        distinction_count += 1

# Step 7: Display results
print("\n--- Student Result Analysis ---")
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Average Marks:", average_marks)
print("Number of students passed:", pass_count)
print("Number of students with distinction:", distinction_count)