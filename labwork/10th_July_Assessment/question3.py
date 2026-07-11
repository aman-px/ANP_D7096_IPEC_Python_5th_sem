employees = {}

for i in range(5):
    print("Enter Details of Employee", i + 1)

    emp_id = input("Employee ID : ")
    name = input("Employee Name : ")
    salary = int(input("Employee Salary : "))

    employees[emp_id] = {
        "name": name,
        "salary": salary
    }

print("\nEmployee Details")
total_salary = 0
highest_salary = 0

for emp_id in employees:
    print(emp_id, employees[emp_id]["name"], employees[emp_id]["salary"])

    total_salary = total_salary + employees[emp_id]["salary"]

    if employees[emp_id]["salary"] > highest_salary:
        highest_salary = employees[emp_id]["salary"]
        
	average_salary = total_salary / len(employees)

print("\nHighest Salary")
print(highest_name, highest_salary)

print("\nAverage Salary")
print(average_salary)
