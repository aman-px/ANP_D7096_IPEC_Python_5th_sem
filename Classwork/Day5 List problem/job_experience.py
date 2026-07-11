print("Enter the name and experience of 5 employees :")
employees = []

for i in range(5):
    name = input("Enter the name of employee : ")
    experience = int(input("Enter the experience of employee (in year ):"))
    if experience < 0:
        exit("Experience must be positive :")
    employees.append({"Name":name,"Experience":experience})

print("List is :",employees)

for i in range(5):
    if employees[i]["Experience"] > 5:
        print(employees[i]["Name"]," : Is Eligible for Bonus Salary ")

