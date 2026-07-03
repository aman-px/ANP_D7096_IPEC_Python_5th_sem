# To create a tuple from the list and print all odd numbers from the tuple
print("Enter any 15 numbers :")
# Creating a blank list to store the numbers
list = []

for i in range(15):
    # taking input from user :
    num = int(input())
    # appending the number to the list:
    list.append(num)

# displaying the list :
print("List is :",list)

# converting the list to tuple:
tpl = tuple(list)

# displaying the tuple:
print("Tuple is :",tpl)


# Displaying odd numbers from the tuple:
print("Odd numbers from the tuple are : ")
for i in tpl:
    if i % 2 ==1:
        print(i,end = ",")
