print("Enter any 20 number : ")
numbers = []
for i in range(20):
    num = int(input())
    numbers.append(num)
print("Enter the Number to match from list  : ")
num1 = int(input())

freq = numbers.count(num1)
if(freq == 0):
    print(num1 ,"not found")
elif(freq == 1):
    print("No duplicates found")
else:
    numbers.reverse()
    for x in range(1,freq):
        numbers.remove(num1)
    numbers.reverse()

print("List after removing duplicate element : ",numbers)

