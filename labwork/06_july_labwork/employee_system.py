# Dictionary of employees
employees = {
    101: {"Name": "Rahul", "Department": "HR", "Salary": 30000},
    102: {"Name": "Priya", "Department": "IT", "Salary": 40000},
    103: {"Name": "Amit", "Department": "Sales", "Salary": 35000},
    104: {"Name": "Neha", "Department": "IT", "Salary": 45000},
    105: {"Name": "Rohan", "Department": "HR", "Salary": 32000}
}

# ------------------------------------
# 1. Display all employee details
# ------------------------------------
print("Employee Details:\n")

for emp_id, details in employees.items():
    print("Employee ID:", emp_id)
    print("Name:", details["Name"])
    print("Department:", details["Department"])
    print("Salary:", details["Salary"])
    print()

# ------------------------------------
# 2. Search employee by Employee ID
# ------------------------------------
search_id = int(input("Enter Employee ID to search: "))

if search_id in employees:
    print("\nEmployee Found")
    print("Name:", employees[search_id]["Name"])
    print("Department:", employees[search_id]["Department"])
    print("Salary:", employees[search_id]["Salary"])
else:
    print("Employee Not Found")

# ------------------------------------
# 3. Increase salary of all employees by 10%
# ------------------------------------
for emp_id in employees:
    employees[emp_id]["Salary"] = employees[emp_id]["Salary"] * 1.10

print("\nSalary increased by 10%.")

# ------------------------------------
# 4. Display employees of a department
# ------------------------------------
department = input("\nEnter Department Name: ")

print("\nEmployees in", department, "Department:\n")

for emp_id, details in employees.items():
    if details["Department"].lower() == department.lower():
        print("Employee ID:", emp_id)
        print("Name:", details["Name"])
        print("Salary:", details["Salary"])
        print()