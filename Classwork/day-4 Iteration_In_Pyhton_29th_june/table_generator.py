# Multiplication Table Generator

# Step 1: Take input from the user
num = int(input("Enter Number: "))

# Step 2: Use a for loop to generate table up to 20
for i in range(1, 21):
    print(num, "x", i, "=", num * i)