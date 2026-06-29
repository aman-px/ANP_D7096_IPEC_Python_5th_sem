# Employee Salary Statistics Program

# Step 1: Accept number of employees
n = int(input("Enter number of employees: "))

# Step 2: Create an empty list to store salaries
salaries = []

# Step 3: Accept salary of each employee
for i in range(n):
    sal = int(input(f"Enter salary of employee {i+1}: "))
    salaries.append(sal)

# Step 4: Calculate highest salary
highest_salary = max(salaries)

# Step 5: Calculate lowest salary
lowest_salary = min(salaries)

# Step 6: Calculate average salary
average_salary = sum(salaries) / n

# Step 7: Count employees earning more than 50000
count_above_50000 = 0
for sal in salaries:
    if sal > 50000:
        count_above_50000 += 1

# Step 8: Display results
print("\n--- Employee Salary Statistics ---")
print("Highest Salary: ₹", highest_salary)
print("Lowest Salary: ₹", lowest_salary)
print("Average Salary: ₹", average_salary)
print("Employees earning more than ₹50,000:", count_above_50000)