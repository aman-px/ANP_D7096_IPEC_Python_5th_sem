# program to accept the total bill amount from the user and display the final amount to 
# be paid.
total_bill = float(input("Enter the total electricity bill :"))
# to validate electricity bill 

if(total_bill < 0):
    exit("Amount should be positive")

# to verify the electricity bill
if(total_bill >= 5000):
    print(" discount applied : ")
    print("Final Bill Amount is : ",total_bill-(total_bill*0.1))
else:
    print("No Discount Applied ")
    print("kareighdklgjdkgd")
    print("FInal bill amount is : ",total_bill)
