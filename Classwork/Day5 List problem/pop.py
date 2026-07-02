# To Insert element in list and remove the element from specific position

#Creating an empty list

numbers = []
print("Enter any 10 Number : ")

for i in range(10):
    num = int(input())
    numbers.append(num)

print("Elements In List Are : ",numbers)

for i in range(0,len(numbers)):
    if numbers[i] % 2 == 1:
        removed = numbers.pop(i)
        print("Removed Elements are : ",removed)
        
print("List After popping :",numbers)

