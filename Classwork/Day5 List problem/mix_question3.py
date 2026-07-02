prices = [450,1200,800,300,1500]
print("Original list of prices:", prices)

price = int(input("Enter the new price to add in list: "))
prices.append(price) 

print("List after adding new price:", prices)

prices[2] = 200

print("List after modifying the price at index 2:", prices)
prices.sort()
print("List after sorting the prices:", prices)
prices.reverse()
print("List after reversing the prices:", prices)
prices.pop(1)
print("List after removing second highest price from lst :",prices)

print("Final List Is :",prices)
