# Electricity Bill Analysis Program

# Step 1: Take number of houses
n = int(input("Enter number of houses: "))

# Step 2: Create an empty list to store units
units = []

# Step 3: Accept units for each house
for i in range(n):
    u = int(input("Enter units consumed by house {i+1}: "))
    units.append(u)

# Step 4: Calculate total units
total_units = sum(units)

# Step 5: Calculate average units
average_units = total_units / n

# Step 6: Find highest and lowest consumption
highest_units = max(units)
lowest_units = min(units)

# Step 7: Display results
print("\n--- Electricity Consumption Analysis ---")
print("Total units consumed:", total_units)
print("Average units consumed:", average_units)
print("Highest consumption:", highest_units)
print("Lowest consumption:", lowest_units)