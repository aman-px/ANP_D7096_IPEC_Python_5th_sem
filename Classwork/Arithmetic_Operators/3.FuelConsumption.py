# Inputs: Total distance covered in kilometers and fuel consumed in liters
distance_traveled = float(input("Enter total distance traveled (in km): "))  # Data Type: float
fuel_consumed = float(input("Enter fuel consumed (in liters): "))  # Data Type: float

# Calculation: Dividing distance by fuel to find mileage (km/l)
mileage = distance_traveled / fuel_consumed  # Operator: /

# Output: Displaying the car's average mileage
print("Car Mileage: ",mileage ,"km/l")