# Inputs: Original retail price and flat discount amount
product_price = float(input("Enter product price: "))    # Data Type: float
discount_amount = float(input("Enter discount amount: "))  # Data Type: float

# Calculation: Subtracting the discount from the original price
final_price = product_price - discount_amount  # Operator: -

# Output: Displaying the checkout price
print(f"Final Price: ${final_price:.2f}")