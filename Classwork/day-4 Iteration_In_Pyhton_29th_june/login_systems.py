# Login System with Maximum Attempts

# Correct credentials
correct_username = "admin"
correct_password = "python123"

# Maximum attempts allowed
max_attempts = 3

# Attempt counter
attempt = 1

# Login process
while attempt <= max_attempts:
    print(f"\nAttempt {attempt}")
    username = input("Username: ")
    password = input("Password: ")

    # Check credentials
    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        attempt += 1

# If all attempts are used
if attempt > max_attempts:
    print("\nAccount Locked")