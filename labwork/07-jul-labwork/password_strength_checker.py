# Function to check password strength
def check_password(password):
    if len(password) < 8:
        return "Weak Password"

    has_upper = False
    has_lower = False
    has_digit = False

    for ch in password:
        if 'A' <= ch <= 'Z':
            has_upper = True
        elif 'a' <= ch <= 'z':
            has_lower = True
        elif '0' <= ch <= '9':
            has_digit = True

    if has_upper and has_lower and has_digit:
        return "Strong Password"
    else:
        return "Weak Password"


# Main Program
password = input("Enter your password: ")

result = check_password(password)

print(result)