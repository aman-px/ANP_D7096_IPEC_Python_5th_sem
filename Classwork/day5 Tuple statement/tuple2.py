print("Enter any 5 prices of products :")
list = []

for i in range(5):
    # taking input from user :
    price = float(input("Enter the price of product : "))
    name = input("Enter the name of the product: ")
    # appending the price to the list:
    list.append({"name": name, "price": price})

# displaying the list :
print("List is :",list)

tpl = tuple(list)

# displaying the tuple:
print("Tuple is :",tpl)

count = 0
for item in range(len(tpl)):
    if tpl[item]["price"] > 4000:
        count = count + 1


print("Number of products with price greater than 4000 is :",count)

min_product = tpl[0]
max_product = tpl[0]

for product in tpl:
    if product["price"] < min_product["price"]:
        min_product = product

    if product["price"] > max_product["price"]:
        max_product = product

print("Lowest price product:", min_product["name"], "Price:", min_product["price"])
print("Highest price product:", max_product["name"], "Price:", max_product["price"])

