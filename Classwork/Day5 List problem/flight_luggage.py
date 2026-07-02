print("Enter the name of 5 passenger and their luggage weight : ")
passengers = []
for i in range(5):
    name = input("Enter the name of passenger : ")
    weight = float(input("Enter the weight of luggage ( in kg ): "))
    if weight < 0:
        exit("Weight should be a positive number ")
    passengers.append({"name":name,"weight":weight})

print(passengers,"List Of flight attendent:  ")

for passenger in passengers:
    if passenger["weight"] > 15:
        print(passenger["name"], " Your Luggage weight is more than 15 kg, please pay extra charges : ")
 