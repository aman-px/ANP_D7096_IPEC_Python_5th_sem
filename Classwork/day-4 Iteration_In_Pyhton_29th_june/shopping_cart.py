# Shopping Cart Billing System

# Step 1: Accept number of products
n = int(input("Enter number of products: "))

# Variables to store calculations
total_bill = 0
product_costs = []

most_expensive_cost = 0
most_expensive_product = ""

cheapest_cost = None
cheapest_product = ""

# Step 2: Loop to accept product details
for i in range(1, n + 1):
    print(f"\nEnter details for Product {i}:")
    
    product_name = input("Product Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per Unit: "))

    # Step 3: Calculate individual product cost
    cost = quantity * price
    product_costs.append(cost)

    # Display individual product cost
    print(f"Cost of {product_name}: ₹{cost:.2f}")

    # Add to total bill
    total_bill += cost

    # Step 4: Find most expensive product
    if cost > most_expensive_cost:
        most_expensive_cost = cost
        most_expensive_product = product_name

    # Step 5: Find cheapest product
    if cheapest_cost is None or cost < cheapest_cost:
        cheapest_cost = cost
        cheapest_product = product_name

# Step 6: Calculate average product cost
average_cost = total_bill / n

# Step 7: Display final results
print("\n------ BILL SUMMARY ------")
print(f"Total Bill Amount: ₹{total_bill:.2f}")
print(f"Most Expensive Product: {most_expensive_product} (₹{most_expensive_cost:.2f})")
print(f"Cheapest Product: {cheapest_product} (₹{cheapest_cost:.2f})")
print(f"Average Product Cost: ₹{average_cost:.2f}")