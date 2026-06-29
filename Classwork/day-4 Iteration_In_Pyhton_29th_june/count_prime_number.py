# Program to display and count prime numbers in a given range

# Step 1: Take input from the user
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

# Step 2: Initialize counter
prime_count = 0

print("Prime numbers in the given range are:")

# Step 3: Loop through the range
for num in range(start, end + 1):

    # Prime numbers are greater than 1
    if num > 1:
        is_prime = True

        # Step 4: Check if num is prime
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        # Step 5: If prime, print and count
        if is_prime:
            print(num)
            prime_count += 1

# Step 6: Display total count
print("Total prime numbers:", prime_count)