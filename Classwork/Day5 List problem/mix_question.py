print("Enter any 5 integers :")
numbers = []

for i in range(5):
    num = int(input("Enter the number:"))
    numbers.append(num)

print("List before appending one extra number is :",numbers)

num1 = int(input("Enter one extra  number to append in List :"))
numbers.append(num1)

print("List Is :",numbers)

numbers[2] = 100

print("List After Modification Is :",numbers)

numbers.sort()

print("List After Sorting Is :",numbers)

numbers.reverse()

print("List After Reversing Is :",numbers)

numbers.pop(5)

print("List After Popping Element at Index 5 Is :",numbers)

print("Final List Is : ", numbers)
