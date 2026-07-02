print("Enter the name and salary of 5 persons : ")
persons = []
for i in range(5):
    name = input("Enter the name of person : ")
    salary = float(input("Enter the salary ( in per annum ): "))
    persons.append({"name": name, "salary": salary})

print(persons,"List Of Persons")

for person in persons:
    if person["salary"] > 500000:
        print(person["name"])



