
# Password Strength Checker Program

# Infinite loop to keep asking for password
while True:
    # Taking password input from the user
    password = input("Enter Password: ")

    # Checking the length of the password
    if len(password) >= 8:
        # If password length is 8 or more
        print("Password Accepted.")
        break   # Exit the loop
    else:
        # If password length is less than 8
        print("Password too short.")