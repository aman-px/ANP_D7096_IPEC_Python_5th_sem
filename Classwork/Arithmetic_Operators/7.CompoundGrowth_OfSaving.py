# Inputs: Initial investment amount and the timeline in years
initial_amount = float(input("Enter initial amount: "))  # Data Type: float
number_of_years = int(input("Enter number of years: "))  # Data Type: int

# Calculation: Multiplying by 2 raised to the power of the number of years
# Formula: Final Amount = Initial Amount * (2 ^ Years)
final_amount = initial_amount * (2 ** number_of_years)  # Operators: ** and *

# Output: Displaying the accumulated final amount
print(f"Final Amount after {number_of_years} years: ${final_amount:.2f}")