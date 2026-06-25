<<<<<<< HEAD
# Inputs: Total number of students and how many students sit in each row
total_students = int(input("Enter total number of students: "))  # Data Type: int
students_per_row = int(input("Enter students per row: "))        # Data Type: int

# Calculation: Floor division (//) determines how many *complete* rows fit perfectly
complete_rows = total_students // students_per_row  # Operator: //

# Output: Displaying the number of complete rows formed
=======
# Inputs: Total number of students and how many students sit in each row
total_students = int(input("Enter total number of students: "))  # Data Type: int
students_per_row = int(input("Enter students per row: "))        # Data Type: int

# Calculation: Floor division (//) determines how many *complete* rows fit perfectly
complete_rows = total_students // students_per_row  # Operator: //

# Output: Displaying the number of complete rows formed
>>>>>>> ae48300 (instructions for self learning)
print(f"Number of Complete Rows: {complete_rows}")