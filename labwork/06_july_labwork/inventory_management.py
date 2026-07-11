# Dictionary to store product stock
products = {
    "Laptop": 15,
    "Mouse": 40,
    "Keyboard": 25,
    "Monitor": 10
}

# ---------------------------------
# 1. Display current products
# ---------------------------------
print("Current Products:")
for product, stock in products.items():
    print(product, ":", stock)

# ---------------------------------
# 2. Add a new product
# ---------------------------------
new_product = input("\nEnter new product name: ")
new_stock = int(input("Enter stock: "))

products[new_product] = new_stock
print("Product added successfully!")

# ---------------------------------
# 3. Update stock of an existing product
# ---------------------------------
update_product = input("\nEnter product name to update: ")

if update_product in products:
    updated_stock = int(input("Enter new stock: "))
    products[update_product] = updated_stock
    print("Stock updated successfully!")
else:
    print("Product not found!")

# ---------------------------------
# 4. Remove a product
# ---------------------------------
remove_product = input("\nEnter product name to remove: ")

if remove_product in products:
    del products[remove_product]
    print("Product removed successfully!")
else:
    print("Product not found!")

# ---------------------------------
# 5. Display products with stock less than 20
# ---------------------------------
print("\nProducts with stock less than 20:")

for product, stock in products.items():
    if stock < 20:
        print(product, ":", stock)

# ---------------------------------
# 6. Display total stock in inventory
# ---------------------------------
total_stock = sum(products.values())

print("\nTotal Items Available in Inventory:", total_stock)