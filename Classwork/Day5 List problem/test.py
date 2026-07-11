print("Enter any 10 number :")
# Creating a blank list :
list = []

for i in range(10):
    # Taking input from user and appending it to the list
    num = int(input("Enter the number:"))
    list.append(num)
# List after appending value to list :
print("List is : ",list)
# To arrange the ascending order , we will use sort method :
list.sort()
# then reversing list to get elements in decending order:
print("List After Sorting Is :",list)

list.reverse() 

print("List After Reversing Is :",list)

# To display the 3rd greatest element from list

print("The 3rd greatest number in the list is : ", list[2])