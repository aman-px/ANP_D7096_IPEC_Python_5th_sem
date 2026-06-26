# To Check whether a person can vote or not

age = float(input("Enter the age of person : "))
 # to validate the age 
if(age<=0):
    exit("Age must be positive")

# To Verify Eligibility

if(age >= 18):
    print("Person is eligible to vote ")
else:
    print("Person is not eligible to vote ")