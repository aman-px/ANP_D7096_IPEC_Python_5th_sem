<<<<<<< HEAD
# Inputs: Unit cost per gigabyte and the total number of gigabytes required
cost_per_gb = float(input("Enter cost per GB: "))    # Data Type: float
number_of_gbs = float(input("Enter number of GBs: "))  # Data Type: float

# Calculation: Multiplying unit cost by total data volume
total_recharge_cost = cost_per_gb * number_of_gbs  # Operator: *

# Output: Displaying the total bill for the mobile data pack
=======
# Inputs: Unit cost per gigabyte and the total number of gigabytes required
cost_per_gb = float(input("Enter cost per GB: "))    # Data Type: float
number_of_gbs = float(input("Enter number of GBs: "))  # Data Type: float

# Calculation: Multiplying unit cost by total data volume
total_recharge_cost = cost_per_gb * number_of_gbs  # Operator: *

# Output: Displaying the total bill for the mobile data pack
>>>>>>> ae48300 (instructions for self learning)
print(f"Total Recharge Cost: ${total_recharge_cost:.2f}")