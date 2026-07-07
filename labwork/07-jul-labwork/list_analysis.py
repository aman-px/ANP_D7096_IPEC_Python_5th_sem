# Function to find maximum value
def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

def find_average(numbers):
    total = 0
    count = 0

    for num in numbers:
        total += num
        count += 1

    return total / count

# Main Program
numbers = []

print("Enter 10 integers:")
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

maximum = find_max(numbers)
minimum = find_min(numbers)
average = find_average(numbers)

print("\nList:", numbers)
print("Maximum Value:", maximum)
print("Minimum Value:", minimum)
print("Average Value:", average)